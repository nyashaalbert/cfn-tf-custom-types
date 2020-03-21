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
    Id: Optional[str]
    ListenerId: Optional[str]
    LoadBalancerId: Optional[str]
    Port: Optional[float]
    PrivateIp: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Port=json_data.get("Port"),
            PrivateIp=json_data.get("PrivateIp"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

