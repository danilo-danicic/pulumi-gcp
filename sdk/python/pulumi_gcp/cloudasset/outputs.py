# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'FolderFeedFeedOutputConfig',
    'FolderFeedFeedOutputConfigPubsubDestination',
    'OrganizationFeedFeedOutputConfig',
    'OrganizationFeedFeedOutputConfigPubsubDestination',
    'ProjectFeedFeedOutputConfig',
    'ProjectFeedFeedOutputConfigPubsubDestination',
]

@pulumi.output_type
class FolderFeedFeedOutputConfig(dict):
    def __init__(__self__, *,
                 pubsub_destination: 'outputs.FolderFeedFeedOutputConfigPubsubDestination'):
        """
        :param 'FolderFeedFeedOutputConfigPubsubDestinationArgs' pubsub_destination: Destination on Cloud Pubsub.
               Structure is documented below.
        """
        pulumi.set(__self__, "pubsub_destination", pubsub_destination)

    @property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> 'outputs.FolderFeedFeedOutputConfigPubsubDestination':
        """
        Destination on Cloud Pubsub.
        Structure is documented below.
        """
        return pulumi.get(self, "pubsub_destination")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FolderFeedFeedOutputConfigPubsubDestination(dict):
    def __init__(__self__, *,
                 topic: str):
        """
        :param str topic: Destination on Cloud Pubsub topic.
        """
        pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def topic(self) -> str:
        """
        Destination on Cloud Pubsub topic.
        """
        return pulumi.get(self, "topic")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OrganizationFeedFeedOutputConfig(dict):
    def __init__(__self__, *,
                 pubsub_destination: 'outputs.OrganizationFeedFeedOutputConfigPubsubDestination'):
        """
        :param 'OrganizationFeedFeedOutputConfigPubsubDestinationArgs' pubsub_destination: Destination on Cloud Pubsub.
               Structure is documented below.
        """
        pulumi.set(__self__, "pubsub_destination", pubsub_destination)

    @property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> 'outputs.OrganizationFeedFeedOutputConfigPubsubDestination':
        """
        Destination on Cloud Pubsub.
        Structure is documented below.
        """
        return pulumi.get(self, "pubsub_destination")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OrganizationFeedFeedOutputConfigPubsubDestination(dict):
    def __init__(__self__, *,
                 topic: str):
        """
        :param str topic: Destination on Cloud Pubsub topic.
        """
        pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def topic(self) -> str:
        """
        Destination on Cloud Pubsub topic.
        """
        return pulumi.get(self, "topic")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectFeedFeedOutputConfig(dict):
    def __init__(__self__, *,
                 pubsub_destination: 'outputs.ProjectFeedFeedOutputConfigPubsubDestination'):
        """
        :param 'ProjectFeedFeedOutputConfigPubsubDestinationArgs' pubsub_destination: Destination on Cloud Pubsub.
               Structure is documented below.
        """
        pulumi.set(__self__, "pubsub_destination", pubsub_destination)

    @property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> 'outputs.ProjectFeedFeedOutputConfigPubsubDestination':
        """
        Destination on Cloud Pubsub.
        Structure is documented below.
        """
        return pulumi.get(self, "pubsub_destination")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectFeedFeedOutputConfigPubsubDestination(dict):
    def __init__(__self__, *,
                 topic: str):
        """
        :param str topic: Destination on Cloud Pubsub topic.
        """
        pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def topic(self) -> str:
        """
        Destination on Cloud Pubsub topic.
        """
        return pulumi.get(self, "topic")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

