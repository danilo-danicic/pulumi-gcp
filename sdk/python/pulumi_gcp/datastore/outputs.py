# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'DataStoreIndexProperty',
]

@pulumi.output_type
class DataStoreIndexProperty(dict):
    def __init__(__self__, *,
                 direction: str,
                 name: str):
        """
        :param str direction: The direction the index should optimize for sorting.
               Possible values are `ASCENDING` and `DESCENDING`.
        :param str name: The property name to index.
        """
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def direction(self) -> str:
        """
        The direction the index should optimize for sorting.
        Possible values are `ASCENDING` and `DESCENDING`.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The property name to index.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


