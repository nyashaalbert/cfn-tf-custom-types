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
    GlobalDefault: Optional[bool]
    Id: Optional[str]
    Value: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]

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
            GlobalDefault=json_data.get("GlobalDefault"),
            Id=json_data.get("Id"),
            Value=json_data.get("Value"),
            Metadata=json_data.get("Metadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Annotations: Optional[Sequence["_Annotations"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Annotations=json_data.get("Annotations"),
            GenerateName=json_data.get("GenerateName"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Annotations:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels

