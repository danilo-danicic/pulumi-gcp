# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GameServerClusterConnectionInfo',
    'GameServerClusterConnectionInfoGkeClusterReference',
    'GameServerConfigFleetConfig',
    'GameServerConfigScalingConfig',
    'GameServerConfigScalingConfigSchedule',
    'GameServerConfigScalingConfigSelector',
    'GameServerDeploymentRolloutGameServerConfigOverride',
    'GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelector',
    'GetGameServerDeploymentRolloutGameServerConfigOverrideResult',
    'GetGameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorResult',
]

@pulumi.output_type
class GameServerClusterConnectionInfo(dict):
    def __init__(__self__, *,
                 gke_cluster_reference: 'outputs.GameServerClusterConnectionInfoGkeClusterReference',
                 namespace: str):
        """
        :param 'GameServerClusterConnectionInfoGkeClusterReferenceArgs' gke_cluster_reference: Reference of the GKE cluster where the game servers are installed.
               Structure is documented below.
        :param str namespace: Namespace designated on the game server cluster where the game server
               instances will be created. The namespace existence will be validated
               during creation.
        """
        pulumi.set(__self__, "gke_cluster_reference", gke_cluster_reference)
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="gkeClusterReference")
    def gke_cluster_reference(self) -> 'outputs.GameServerClusterConnectionInfoGkeClusterReference':
        """
        Reference of the GKE cluster where the game servers are installed.
        Structure is documented below.
        """
        return pulumi.get(self, "gke_cluster_reference")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        Namespace designated on the game server cluster where the game server
        instances will be created. The namespace existence will be validated
        during creation.
        """
        return pulumi.get(self, "namespace")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerClusterConnectionInfoGkeClusterReference(dict):
    def __init__(__self__, *,
                 cluster: str):
        """
        :param str cluster: The full or partial name of a GKE cluster, using one of the following
               forms:
               * `projects/{project_id}/locations/{location}/clusters/{cluster_id}`
               * `locations/{location}/clusters/{cluster_id}`
               * `{cluster_id}`
               If project and location are not specified, the project and location of the
               GameServerCluster resource are used to generate the full name of the
               GKE cluster.
        """
        pulumi.set(__self__, "cluster", cluster)

    @property
    @pulumi.getter
    def cluster(self) -> str:
        """
        The full or partial name of a GKE cluster, using one of the following
        forms:
        * `projects/{project_id}/locations/{location}/clusters/{cluster_id}`
        * `locations/{location}/clusters/{cluster_id}`
        * `{cluster_id}`
        If project and location are not specified, the project and location of the
        GameServerCluster resource are used to generate the full name of the
        GKE cluster.
        """
        return pulumi.get(self, "cluster")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerConfigFleetConfig(dict):
    def __init__(__self__, *,
                 fleet_spec: str,
                 name: Optional[str] = None):
        """
        :param str fleet_spec: The fleet spec, which is sent to Agones to configure fleet.
               The spec can be passed as inline json but it is recommended to use a file reference
               instead. File references can contain the json or yaml format of the fleet spec. Eg:
               * fleet_spec = jsonencode(yamldecode(file("fleet_configs.yaml")))
               * fleet_spec = file("fleet_configs.json")
               The format of the spec can be found :
               `https://agones.dev/site/docs/reference/fleet/`.
        :param str name: The name of the ScalingConfig
        """
        pulumi.set(__self__, "fleet_spec", fleet_spec)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="fleetSpec")
    def fleet_spec(self) -> str:
        """
        The fleet spec, which is sent to Agones to configure fleet.
        The spec can be passed as inline json but it is recommended to use a file reference
        instead. File references can contain the json or yaml format of the fleet spec. Eg:
        * fleet_spec = jsonencode(yamldecode(file("fleet_configs.yaml")))
        * fleet_spec = file("fleet_configs.json")
        The format of the spec can be found :
        `https://agones.dev/site/docs/reference/fleet/`.
        """
        return pulumi.get(self, "fleet_spec")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the ScalingConfig
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerConfigScalingConfig(dict):
    def __init__(__self__, *,
                 fleet_autoscaler_spec: str,
                 name: str,
                 schedules: Optional[Sequence['outputs.GameServerConfigScalingConfigSchedule']] = None,
                 selectors: Optional[Sequence['outputs.GameServerConfigScalingConfigSelector']] = None):
        """
        :param str fleet_autoscaler_spec: Fleet autoscaler spec, which is sent to Agones.
               Example spec can be found :
               https://agones.dev/site/docs/reference/fleetautoscaler/
        :param str name: The name of the ScalingConfig
        :param Sequence['GameServerConfigScalingConfigScheduleArgs'] schedules: The schedules to which this scaling config applies.
               Structure is documented below.
        :param Sequence['GameServerConfigScalingConfigSelectorArgs'] selectors: Labels used to identify the clusters to which this scaling config
               applies. A cluster is subject to this scaling config if its labels match
               any of the selector entries.
               Structure is documented below.
        """
        pulumi.set(__self__, "fleet_autoscaler_spec", fleet_autoscaler_spec)
        pulumi.set(__self__, "name", name)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if selectors is not None:
            pulumi.set(__self__, "selectors", selectors)

    @property
    @pulumi.getter(name="fleetAutoscalerSpec")
    def fleet_autoscaler_spec(self) -> str:
        """
        Fleet autoscaler spec, which is sent to Agones.
        Example spec can be found :
        https://agones.dev/site/docs/reference/fleetautoscaler/
        """
        return pulumi.get(self, "fleet_autoscaler_spec")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the ScalingConfig
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedules(self) -> Optional[Sequence['outputs.GameServerConfigScalingConfigSchedule']]:
        """
        The schedules to which this scaling config applies.
        Structure is documented below.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def selectors(self) -> Optional[Sequence['outputs.GameServerConfigScalingConfigSelector']]:
        """
        Labels used to identify the clusters to which this scaling config
        applies. A cluster is subject to this scaling config if its labels match
        any of the selector entries.
        Structure is documented below.
        """
        return pulumi.get(self, "selectors")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerConfigScalingConfigSchedule(dict):
    def __init__(__self__, *,
                 cron_job_duration: Optional[str] = None,
                 cron_spec: Optional[str] = None,
                 end_time: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        :param str cron_job_duration: The duration for the cron job event. The duration of the event is effective
               after the cron job's start time.
               A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
        :param str cron_spec: The cron definition of the scheduled event. See
               https://en.wikipedia.org/wiki/Cron. Cron spec specifies the local time as
               defined by the realm.
        :param str end_time: The end time of the event.
               A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        :param str start_time: The start time of the event.
               A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        if cron_job_duration is not None:
            pulumi.set(__self__, "cron_job_duration", cron_job_duration)
        if cron_spec is not None:
            pulumi.set(__self__, "cron_spec", cron_spec)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="cronJobDuration")
    def cron_job_duration(self) -> Optional[str]:
        """
        The duration for the cron job event. The duration of the event is effective
        after the cron job's start time.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
        """
        return pulumi.get(self, "cron_job_duration")

    @property
    @pulumi.getter(name="cronSpec")
    def cron_spec(self) -> Optional[str]:
        """
        The cron definition of the scheduled event. See
        https://en.wikipedia.org/wiki/Cron. Cron spec specifies the local time as
        defined by the realm.
        """
        return pulumi.get(self, "cron_spec")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        The end time of the event.
        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        The start time of the event.
        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "start_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerConfigScalingConfigSelector(dict):
    def __init__(__self__, *,
                 labels: Optional[Mapping[str, str]] = None):
        """
        :param Mapping[str, str] labels: Set of labels to group by.
        """
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, str]]:
        """
        Set of labels to group by.
        """
        return pulumi.get(self, "labels")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerDeploymentRolloutGameServerConfigOverride(dict):
    def __init__(__self__, *,
                 config_version: Optional[str] = None,
                 realms_selector: Optional['outputs.GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelector'] = None):
        """
        :param str config_version: Version of the configuration.
        :param 'GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorArgs' realms_selector: Selection by realms.
               Structure is documented below.
        """
        if config_version is not None:
            pulumi.set(__self__, "config_version", config_version)
        if realms_selector is not None:
            pulumi.set(__self__, "realms_selector", realms_selector)

    @property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> Optional[str]:
        """
        Version of the configuration.
        """
        return pulumi.get(self, "config_version")

    @property
    @pulumi.getter(name="realmsSelector")
    def realms_selector(self) -> Optional['outputs.GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelector']:
        """
        Selection by realms.
        Structure is documented below.
        """
        return pulumi.get(self, "realms_selector")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelector(dict):
    def __init__(__self__, *,
                 realms: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] realms: List of realms to match against.
        """
        if realms is not None:
            pulumi.set(__self__, "realms", realms)

    @property
    @pulumi.getter
    def realms(self) -> Optional[Sequence[str]]:
        """
        List of realms to match against.
        """
        return pulumi.get(self, "realms")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetGameServerDeploymentRolloutGameServerConfigOverrideResult(dict):
    def __init__(__self__, *,
                 config_version: str,
                 realms_selectors: Sequence['outputs.GetGameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorResult']):
        pulumi.set(__self__, "config_version", config_version)
        pulumi.set(__self__, "realms_selectors", realms_selectors)

    @property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> str:
        return pulumi.get(self, "config_version")

    @property
    @pulumi.getter(name="realmsSelectors")
    def realms_selectors(self) -> Sequence['outputs.GetGameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorResult']:
        return pulumi.get(self, "realms_selectors")


@pulumi.output_type
class GetGameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorResult(dict):
    def __init__(__self__, *,
                 realms: Sequence[str]):
        pulumi.set(__self__, "realms", realms)

    @property
    @pulumi.getter
    def realms(self) -> Sequence[str]:
        return pulumi.get(self, "realms")


