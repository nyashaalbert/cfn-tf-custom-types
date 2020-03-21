# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    ClusterVersion: Optional[str]
    HttpsEndpoint: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SshEndpoint: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Tier: Optional[str]
    ComponentVersion: Optional[Sequence["_ComponentVersion"]]
    Gateway: Optional[Sequence["_Gateway"]]
    Roles: Optional[Sequence["_Roles"]]
    StorageAccount: Optional[Sequence["_StorageAccount"]]
    StorageAccountGen2: Optional[Sequence["_StorageAccountGen2"]]
    Timeouts: Optional["_Timeouts"]
    HeadNode: Optional[Sequence["_HeadNode"]]
    WorkerNode: Optional[Sequence["_WorkerNode"]]
    ZookeeperNode: Optional[Sequence["_ZookeeperNode"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterVersion=json_data.get("ClusterVersion"),
            HttpsEndpoint=json_data.get("HttpsEndpoint"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SshEndpoint=json_data.get("SshEndpoint"),
            Tags=json_data.get("Tags"),
            Tier=json_data.get("Tier"),
            ComponentVersion=json_data.get("ComponentVersion"),
            Gateway=json_data.get("Gateway"),
            Roles=json_data.get("Roles"),
            StorageAccount=json_data.get("StorageAccount"),
            StorageAccountGen2=json_data.get("StorageAccountGen2"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            HeadNode=json_data.get("HeadNode"),
            WorkerNode=json_data.get("WorkerNode"),
            ZookeeperNode=json_data.get("ZookeeperNode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ComponentVersion:
    Kafka: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentVersion"]:
        if not json_data:
            return None
        return cls(
            Kafka=json_data.get("Kafka"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentVersion = ComponentVersion


@dataclass
class Gateway:
    Enabled: Optional[bool]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Gateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gateway"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Gateway = Gateway


@dataclass
class Roles:
    HeadNode: Optional[Sequence["_HeadNode"]]
    WorkerNode: Optional[Sequence["_WorkerNode"]]
    ZookeeperNode: Optional[Sequence["_ZookeeperNode"]]

    @classmethod
    def _deserialize(
        cls: Type["_Roles"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Roles"]:
        if not json_data:
            return None
        return cls(
            HeadNode=json_data.get("HeadNode"),
            WorkerNode=json_data.get("WorkerNode"),
            ZookeeperNode=json_data.get("ZookeeperNode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Roles = Roles


@dataclass
class HeadNode:
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadNode"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshKeys=json_data.get("SshKeys"),
            SubnetId=json_data.get("SubnetId"),
            Username=json_data.get("Username"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            VmSize=json_data.get("VmSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadNode = HeadNode


@dataclass
class WorkerNode:
    MinInstanceCount: Optional[float]
    NumberOfDisksPerNode: Optional[float]
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    TargetInstanceCount: Optional[float]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerNode"]:
        if not json_data:
            return None
        return cls(
            MinInstanceCount=json_data.get("MinInstanceCount"),
            NumberOfDisksPerNode=json_data.get("NumberOfDisksPerNode"),
            Password=json_data.get("Password"),
            SshKeys=json_data.get("SshKeys"),
            SubnetId=json_data.get("SubnetId"),
            TargetInstanceCount=json_data.get("TargetInstanceCount"),
            Username=json_data.get("Username"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            VmSize=json_data.get("VmSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerNode = WorkerNode


@dataclass
class ZookeeperNode:
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZookeeperNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZookeeperNode"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshKeys=json_data.get("SshKeys"),
            SubnetId=json_data.get("SubnetId"),
            Username=json_data.get("Username"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            VmSize=json_data.get("VmSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZookeeperNode = ZookeeperNode


@dataclass
class StorageAccount:
    IsDefault: Optional[bool]
    StorageAccountKey: Optional[str]
    StorageContainerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccount"]:
        if not json_data:
            return None
        return cls(
            IsDefault=json_data.get("IsDefault"),
            StorageAccountKey=json_data.get("StorageAccountKey"),
            StorageContainerId=json_data.get("StorageContainerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccount = StorageAccount


@dataclass
class StorageAccountGen2:
    FilesystemId: Optional[str]
    IsDefault: Optional[bool]
    ManagedIdentityResourceId: Optional[str]
    StorageResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccountGen2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccountGen2"]:
        if not json_data:
            return None
        return cls(
            FilesystemId=json_data.get("FilesystemId"),
            IsDefault=json_data.get("IsDefault"),
            ManagedIdentityResourceId=json_data.get("ManagedIdentityResourceId"),
            StorageResourceId=json_data.get("StorageResourceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccountGen2 = StorageAccountGen2


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts

