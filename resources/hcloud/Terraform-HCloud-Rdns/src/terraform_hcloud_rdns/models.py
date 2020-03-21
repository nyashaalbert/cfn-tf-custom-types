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
    DnsPtr: Optional[str]
    FloatingIpId: Optional[float]
    Id: Optional[str]
    IpAddress: Optional[str]
    ServerId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DnsPtr=json_data.get("DnsPtr"),
            FloatingIpId=json_data.get("FloatingIpId"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            ServerId=json_data.get("ServerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

