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
    AvailabilityZone: Optional[str]
    Cidr: Optional[str]
    DhcpEnable: Optional[bool]
    DnsList: Optional[Sequence[str]]
    GatewayIp: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrimaryDns: Optional[str]
    Region: Optional[str]
    SecondaryDns: Optional[str]
    SubnetId: Optional[str]
    VpcId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Cidr=json_data.get("Cidr"),
            DhcpEnable=json_data.get("DhcpEnable"),
            DnsList=json_data.get("DnsList"),
            GatewayIp=json_data.get("GatewayIp"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrimaryDns=json_data.get("PrimaryDns"),
            Region=json_data.get("Region"),
            SecondaryDns=json_data.get("SecondaryDns"),
            SubnetId=json_data.get("SubnetId"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts

