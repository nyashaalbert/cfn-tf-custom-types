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
    Id: Optional[str]
    LimitType: Optional[str]
    MaxBandwidthAbs: Optional[float]
    MaxBandwidthPercent: Optional[float]
    MinBandwidthAbs: Optional[float]
    MinBandwidthPercent: Optional[float]
    Name: Optional[str]
    PercentSourceType: Optional[str]
    Priority: Optional[float]
    QosId: Optional[str]

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
            Id=json_data.get("Id"),
            LimitType=json_data.get("LimitType"),
            MaxBandwidthAbs=json_data.get("MaxBandwidthAbs"),
            MaxBandwidthPercent=json_data.get("MaxBandwidthPercent"),
            MinBandwidthAbs=json_data.get("MinBandwidthAbs"),
            MinBandwidthPercent=json_data.get("MinBandwidthPercent"),
            Name=json_data.get("Name"),
            PercentSourceType=json_data.get("PercentSourceType"),
            Priority=json_data.get("Priority"),
            QosId=json_data.get("QosId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

