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
    Action: Optional[str]
    EventSourceToken: Optional[str]
    FunctionName: Optional[str]
    Id: Optional[str]
    Principal: Optional[str]
    Qualifier: Optional[str]
    SourceAccount: Optional[str]
    SourceArn: Optional[str]
    StatementId: Optional[str]
    StatementIdPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            EventSourceToken=json_data.get("EventSourceToken"),
            FunctionName=json_data.get("FunctionName"),
            Id=json_data.get("Id"),
            Principal=json_data.get("Principal"),
            Qualifier=json_data.get("Qualifier"),
            SourceAccount=json_data.get("SourceAccount"),
            SourceArn=json_data.get("SourceArn"),
            StatementId=json_data.get("StatementId"),
            StatementIdPrefix=json_data.get("StatementIdPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

