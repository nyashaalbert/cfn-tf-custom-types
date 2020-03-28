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
    Description: Optional[str]
    Fabric: Optional[bool]
    Gateway: Optional[str]
    Id: Optional[str]
    InternetNat: Optional[bool]
    Name: Optional[str]
    ProvisionEndIp: Optional[str]
    ProvisionStartIp: Optional[str]
    Public: Optional[bool]
    Resolvers: Optional[Sequence[str]]
    Routes: Optional[Sequence["_Routes"]]
    Subnet: Optional[str]
    VlanId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Fabric=json_data.get("Fabric"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            InternetNat=json_data.get("InternetNat"),
            Name=json_data.get("Name"),
            ProvisionEndIp=json_data.get("ProvisionEndIp"),
            ProvisionStartIp=json_data.get("ProvisionStartIp"),
            Public=json_data.get("Public"),
            Resolvers=json_data.get("Resolvers"),
            Routes=json_data.get("Routes"),
            Subnet=json_data.get("Subnet"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Routes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Routes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Routes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Routes = Routes

