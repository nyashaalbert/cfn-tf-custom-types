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
    EnableDefaultSecurity: Optional[bool]
    Id: Optional[str]
    InboundDefaultPolicy: Optional[str]
    Name: Optional[str]
    OutboundDefaultPolicy: Optional[str]
    Stateful: Optional[bool]

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
            EnableDefaultSecurity=json_data.get("EnableDefaultSecurity"),
            Id=json_data.get("Id"),
            InboundDefaultPolicy=json_data.get("InboundDefaultPolicy"),
            Name=json_data.get("Name"),
            OutboundDefaultPolicy=json_data.get("OutboundDefaultPolicy"),
            Stateful=json_data.get("Stateful"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

