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
    Name: Optional[str]
    DashItem: Optional[Sequence["_DashItem"]]

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
            Name=json_data.get("Name"),
            DashItem=json_data.get("DashItem"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DashItem:
    DashId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DashItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashItem"]:
        if not json_data:
            return None
        return cls(
            DashId=json_data.get("DashId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashItem = DashItem

