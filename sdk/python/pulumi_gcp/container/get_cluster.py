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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
]

@pulumi.output_type
class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, additional_zones=None, addons_configs=None, authenticator_groups_configs=None, cluster_autoscalings=None, cluster_ipv4_cidr=None, cluster_telemetries=None, database_encryptions=None, default_max_pods_per_node=None, default_snat_statuses=None, description=None, enable_binary_authorization=None, enable_intranode_visibility=None, enable_kubernetes_alpha=None, enable_legacy_abac=None, enable_shielded_nodes=None, enable_tpu=None, endpoint=None, id=None, initial_node_count=None, instance_group_urls=None, ip_allocation_policies=None, label_fingerprint=None, location=None, logging_service=None, maintenance_policies=None, master_authorized_networks_configs=None, master_auths=None, master_version=None, min_master_version=None, monitoring_service=None, name=None, network=None, network_policies=None, networking_mode=None, node_configs=None, node_locations=None, node_pools=None, node_version=None, operation=None, pod_security_policy_configs=None, private_cluster_configs=None, project=None, region=None, release_channels=None, remove_default_node_pool=None, resource_labels=None, resource_usage_export_configs=None, self_link=None, services_ipv4_cidr=None, subnetwork=None, tpu_ipv4_cidr_block=None, vertical_pod_autoscalings=None, workload_identity_configs=None, zone=None):
        if additional_zones and not isinstance(additional_zones, list):
            raise TypeError("Expected argument 'additional_zones' to be a list")
        pulumi.set(__self__, "additional_zones", additional_zones)
        if addons_configs and not isinstance(addons_configs, list):
            raise TypeError("Expected argument 'addons_configs' to be a list")
        pulumi.set(__self__, "addons_configs", addons_configs)
        if authenticator_groups_configs and not isinstance(authenticator_groups_configs, list):
            raise TypeError("Expected argument 'authenticator_groups_configs' to be a list")
        pulumi.set(__self__, "authenticator_groups_configs", authenticator_groups_configs)
        if cluster_autoscalings and not isinstance(cluster_autoscalings, list):
            raise TypeError("Expected argument 'cluster_autoscalings' to be a list")
        pulumi.set(__self__, "cluster_autoscalings", cluster_autoscalings)
        if cluster_ipv4_cidr and not isinstance(cluster_ipv4_cidr, str):
            raise TypeError("Expected argument 'cluster_ipv4_cidr' to be a str")
        pulumi.set(__self__, "cluster_ipv4_cidr", cluster_ipv4_cidr)
        if cluster_telemetries and not isinstance(cluster_telemetries, list):
            raise TypeError("Expected argument 'cluster_telemetries' to be a list")
        pulumi.set(__self__, "cluster_telemetries", cluster_telemetries)
        if database_encryptions and not isinstance(database_encryptions, list):
            raise TypeError("Expected argument 'database_encryptions' to be a list")
        pulumi.set(__self__, "database_encryptions", database_encryptions)
        if default_max_pods_per_node and not isinstance(default_max_pods_per_node, int):
            raise TypeError("Expected argument 'default_max_pods_per_node' to be a int")
        pulumi.set(__self__, "default_max_pods_per_node", default_max_pods_per_node)
        if default_snat_statuses and not isinstance(default_snat_statuses, list):
            raise TypeError("Expected argument 'default_snat_statuses' to be a list")
        pulumi.set(__self__, "default_snat_statuses", default_snat_statuses)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enable_binary_authorization and not isinstance(enable_binary_authorization, bool):
            raise TypeError("Expected argument 'enable_binary_authorization' to be a bool")
        pulumi.set(__self__, "enable_binary_authorization", enable_binary_authorization)
        if enable_intranode_visibility and not isinstance(enable_intranode_visibility, bool):
            raise TypeError("Expected argument 'enable_intranode_visibility' to be a bool")
        pulumi.set(__self__, "enable_intranode_visibility", enable_intranode_visibility)
        if enable_kubernetes_alpha and not isinstance(enable_kubernetes_alpha, bool):
            raise TypeError("Expected argument 'enable_kubernetes_alpha' to be a bool")
        pulumi.set(__self__, "enable_kubernetes_alpha", enable_kubernetes_alpha)
        if enable_legacy_abac and not isinstance(enable_legacy_abac, bool):
            raise TypeError("Expected argument 'enable_legacy_abac' to be a bool")
        pulumi.set(__self__, "enable_legacy_abac", enable_legacy_abac)
        if enable_shielded_nodes and not isinstance(enable_shielded_nodes, bool):
            raise TypeError("Expected argument 'enable_shielded_nodes' to be a bool")
        pulumi.set(__self__, "enable_shielded_nodes", enable_shielded_nodes)
        if enable_tpu and not isinstance(enable_tpu, bool):
            raise TypeError("Expected argument 'enable_tpu' to be a bool")
        pulumi.set(__self__, "enable_tpu", enable_tpu)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if initial_node_count and not isinstance(initial_node_count, int):
            raise TypeError("Expected argument 'initial_node_count' to be a int")
        pulumi.set(__self__, "initial_node_count", initial_node_count)
        if instance_group_urls and not isinstance(instance_group_urls, list):
            raise TypeError("Expected argument 'instance_group_urls' to be a list")
        pulumi.set(__self__, "instance_group_urls", instance_group_urls)
        if ip_allocation_policies and not isinstance(ip_allocation_policies, list):
            raise TypeError("Expected argument 'ip_allocation_policies' to be a list")
        pulumi.set(__self__, "ip_allocation_policies", ip_allocation_policies)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logging_service and not isinstance(logging_service, str):
            raise TypeError("Expected argument 'logging_service' to be a str")
        pulumi.set(__self__, "logging_service", logging_service)
        if maintenance_policies and not isinstance(maintenance_policies, list):
            raise TypeError("Expected argument 'maintenance_policies' to be a list")
        pulumi.set(__self__, "maintenance_policies", maintenance_policies)
        if master_authorized_networks_configs and not isinstance(master_authorized_networks_configs, list):
            raise TypeError("Expected argument 'master_authorized_networks_configs' to be a list")
        pulumi.set(__self__, "master_authorized_networks_configs", master_authorized_networks_configs)
        if master_auths and not isinstance(master_auths, list):
            raise TypeError("Expected argument 'master_auths' to be a list")
        pulumi.set(__self__, "master_auths", master_auths)
        if master_version and not isinstance(master_version, str):
            raise TypeError("Expected argument 'master_version' to be a str")
        pulumi.set(__self__, "master_version", master_version)
        if min_master_version and not isinstance(min_master_version, str):
            raise TypeError("Expected argument 'min_master_version' to be a str")
        pulumi.set(__self__, "min_master_version", min_master_version)
        if monitoring_service and not isinstance(monitoring_service, str):
            raise TypeError("Expected argument 'monitoring_service' to be a str")
        pulumi.set(__self__, "monitoring_service", monitoring_service)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_policies and not isinstance(network_policies, list):
            raise TypeError("Expected argument 'network_policies' to be a list")
        pulumi.set(__self__, "network_policies", network_policies)
        if networking_mode and not isinstance(networking_mode, str):
            raise TypeError("Expected argument 'networking_mode' to be a str")
        pulumi.set(__self__, "networking_mode", networking_mode)
        if node_configs and not isinstance(node_configs, list):
            raise TypeError("Expected argument 'node_configs' to be a list")
        pulumi.set(__self__, "node_configs", node_configs)
        if node_locations and not isinstance(node_locations, list):
            raise TypeError("Expected argument 'node_locations' to be a list")
        pulumi.set(__self__, "node_locations", node_locations)
        if node_pools and not isinstance(node_pools, list):
            raise TypeError("Expected argument 'node_pools' to be a list")
        pulumi.set(__self__, "node_pools", node_pools)
        if node_version and not isinstance(node_version, str):
            raise TypeError("Expected argument 'node_version' to be a str")
        pulumi.set(__self__, "node_version", node_version)
        if operation and not isinstance(operation, str):
            raise TypeError("Expected argument 'operation' to be a str")
        pulumi.set(__self__, "operation", operation)
        if pod_security_policy_configs and not isinstance(pod_security_policy_configs, list):
            raise TypeError("Expected argument 'pod_security_policy_configs' to be a list")
        pulumi.set(__self__, "pod_security_policy_configs", pod_security_policy_configs)
        if private_cluster_configs and not isinstance(private_cluster_configs, list):
            raise TypeError("Expected argument 'private_cluster_configs' to be a list")
        pulumi.set(__self__, "private_cluster_configs", private_cluster_configs)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if release_channels and not isinstance(release_channels, list):
            raise TypeError("Expected argument 'release_channels' to be a list")
        pulumi.set(__self__, "release_channels", release_channels)
        if remove_default_node_pool and not isinstance(remove_default_node_pool, bool):
            raise TypeError("Expected argument 'remove_default_node_pool' to be a bool")
        pulumi.set(__self__, "remove_default_node_pool", remove_default_node_pool)
        if resource_labels and not isinstance(resource_labels, dict):
            raise TypeError("Expected argument 'resource_labels' to be a dict")
        pulumi.set(__self__, "resource_labels", resource_labels)
        if resource_usage_export_configs and not isinstance(resource_usage_export_configs, list):
            raise TypeError("Expected argument 'resource_usage_export_configs' to be a list")
        pulumi.set(__self__, "resource_usage_export_configs", resource_usage_export_configs)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if services_ipv4_cidr and not isinstance(services_ipv4_cidr, str):
            raise TypeError("Expected argument 'services_ipv4_cidr' to be a str")
        pulumi.set(__self__, "services_ipv4_cidr", services_ipv4_cidr)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)
        if tpu_ipv4_cidr_block and not isinstance(tpu_ipv4_cidr_block, str):
            raise TypeError("Expected argument 'tpu_ipv4_cidr_block' to be a str")
        pulumi.set(__self__, "tpu_ipv4_cidr_block", tpu_ipv4_cidr_block)
        if vertical_pod_autoscalings and not isinstance(vertical_pod_autoscalings, list):
            raise TypeError("Expected argument 'vertical_pod_autoscalings' to be a list")
        pulumi.set(__self__, "vertical_pod_autoscalings", vertical_pod_autoscalings)
        if workload_identity_configs and not isinstance(workload_identity_configs, list):
            raise TypeError("Expected argument 'workload_identity_configs' to be a list")
        pulumi.set(__self__, "workload_identity_configs", workload_identity_configs)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="additionalZones")
    def additional_zones(self) -> Sequence[str]:
        return pulumi.get(self, "additional_zones")

    @property
    @pulumi.getter(name="addonsConfigs")
    def addons_configs(self) -> Sequence['outputs.GetClusterAddonsConfigResult']:
        return pulumi.get(self, "addons_configs")

    @property
    @pulumi.getter(name="authenticatorGroupsConfigs")
    def authenticator_groups_configs(self) -> Sequence['outputs.GetClusterAuthenticatorGroupsConfigResult']:
        return pulumi.get(self, "authenticator_groups_configs")

    @property
    @pulumi.getter(name="clusterAutoscalings")
    def cluster_autoscalings(self) -> Sequence['outputs.GetClusterClusterAutoscalingResult']:
        return pulumi.get(self, "cluster_autoscalings")

    @property
    @pulumi.getter(name="clusterIpv4Cidr")
    def cluster_ipv4_cidr(self) -> str:
        return pulumi.get(self, "cluster_ipv4_cidr")

    @property
    @pulumi.getter(name="clusterTelemetries")
    def cluster_telemetries(self) -> Sequence['outputs.GetClusterClusterTelemetryResult']:
        return pulumi.get(self, "cluster_telemetries")

    @property
    @pulumi.getter(name="databaseEncryptions")
    def database_encryptions(self) -> Sequence['outputs.GetClusterDatabaseEncryptionResult']:
        return pulumi.get(self, "database_encryptions")

    @property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> int:
        return pulumi.get(self, "default_max_pods_per_node")

    @property
    @pulumi.getter(name="defaultSnatStatuses")
    def default_snat_statuses(self) -> Sequence['outputs.GetClusterDefaultSnatStatusResult']:
        return pulumi.get(self, "default_snat_statuses")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableBinaryAuthorization")
    def enable_binary_authorization(self) -> bool:
        return pulumi.get(self, "enable_binary_authorization")

    @property
    @pulumi.getter(name="enableIntranodeVisibility")
    def enable_intranode_visibility(self) -> bool:
        return pulumi.get(self, "enable_intranode_visibility")

    @property
    @pulumi.getter(name="enableKubernetesAlpha")
    def enable_kubernetes_alpha(self) -> bool:
        return pulumi.get(self, "enable_kubernetes_alpha")

    @property
    @pulumi.getter(name="enableLegacyAbac")
    def enable_legacy_abac(self) -> bool:
        return pulumi.get(self, "enable_legacy_abac")

    @property
    @pulumi.getter(name="enableShieldedNodes")
    def enable_shielded_nodes(self) -> bool:
        return pulumi.get(self, "enable_shielded_nodes")

    @property
    @pulumi.getter(name="enableTpu")
    def enable_tpu(self) -> bool:
        return pulumi.get(self, "enable_tpu")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> int:
        return pulumi.get(self, "initial_node_count")

    @property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(self) -> Sequence[str]:
        return pulumi.get(self, "instance_group_urls")

    @property
    @pulumi.getter(name="ipAllocationPolicies")
    def ip_allocation_policies(self) -> Sequence['outputs.GetClusterIpAllocationPolicyResult']:
        return pulumi.get(self, "ip_allocation_policies")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="loggingService")
    def logging_service(self) -> str:
        return pulumi.get(self, "logging_service")

    @property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(self) -> Sequence['outputs.GetClusterMaintenancePolicyResult']:
        return pulumi.get(self, "maintenance_policies")

    @property
    @pulumi.getter(name="masterAuthorizedNetworksConfigs")
    def master_authorized_networks_configs(self) -> Sequence['outputs.GetClusterMasterAuthorizedNetworksConfigResult']:
        return pulumi.get(self, "master_authorized_networks_configs")

    @property
    @pulumi.getter(name="masterAuths")
    def master_auths(self) -> Sequence['outputs.GetClusterMasterAuthResult']:
        return pulumi.get(self, "master_auths")

    @property
    @pulumi.getter(name="masterVersion")
    def master_version(self) -> str:
        return pulumi.get(self, "master_version")

    @property
    @pulumi.getter(name="minMasterVersion")
    def min_master_version(self) -> str:
        return pulumi.get(self, "min_master_version")

    @property
    @pulumi.getter(name="monitoringService")
    def monitoring_service(self) -> str:
        return pulumi.get(self, "monitoring_service")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkPolicies")
    def network_policies(self) -> Sequence['outputs.GetClusterNetworkPolicyResult']:
        return pulumi.get(self, "network_policies")

    @property
    @pulumi.getter(name="networkingMode")
    def networking_mode(self) -> str:
        return pulumi.get(self, "networking_mode")

    @property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence['outputs.GetClusterNodeConfigResult']:
        return pulumi.get(self, "node_configs")

    @property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> Sequence[str]:
        return pulumi.get(self, "node_locations")

    @property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Sequence['outputs.GetClusterNodePoolResult']:
        return pulumi.get(self, "node_pools")

    @property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> str:
        return pulumi.get(self, "node_version")

    @property
    @pulumi.getter
    def operation(self) -> str:
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter(name="podSecurityPolicyConfigs")
    def pod_security_policy_configs(self) -> Sequence['outputs.GetClusterPodSecurityPolicyConfigResult']:
        return pulumi.get(self, "pod_security_policy_configs")

    @property
    @pulumi.getter(name="privateClusterConfigs")
    def private_cluster_configs(self) -> Sequence['outputs.GetClusterPrivateClusterConfigResult']:
        return pulumi.get(self, "private_cluster_configs")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="releaseChannels")
    def release_channels(self) -> Sequence['outputs.GetClusterReleaseChannelResult']:
        return pulumi.get(self, "release_channels")

    @property
    @pulumi.getter(name="removeDefaultNodePool")
    def remove_default_node_pool(self) -> bool:
        return pulumi.get(self, "remove_default_node_pool")

    @property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "resource_labels")

    @property
    @pulumi.getter(name="resourceUsageExportConfigs")
    def resource_usage_export_configs(self) -> Sequence['outputs.GetClusterResourceUsageExportConfigResult']:
        return pulumi.get(self, "resource_usage_export_configs")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="servicesIpv4Cidr")
    def services_ipv4_cidr(self) -> str:
        return pulumi.get(self, "services_ipv4_cidr")

    @property
    @pulumi.getter
    def subnetwork(self) -> str:
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter(name="tpuIpv4CidrBlock")
    def tpu_ipv4_cidr_block(self) -> str:
        return pulumi.get(self, "tpu_ipv4_cidr_block")

    @property
    @pulumi.getter(name="verticalPodAutoscalings")
    def vertical_pod_autoscalings(self) -> Sequence['outputs.GetClusterVerticalPodAutoscalingResult']:
        return pulumi.get(self, "vertical_pod_autoscalings")

    @property
    @pulumi.getter(name="workloadIdentityConfigs")
    def workload_identity_configs(self) -> Sequence['outputs.GetClusterWorkloadIdentityConfigResult']:
        return pulumi.get(self, "workload_identity_configs")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        return pulumi.get(self, "zone")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            additional_zones=self.additional_zones,
            addons_configs=self.addons_configs,
            authenticator_groups_configs=self.authenticator_groups_configs,
            cluster_autoscalings=self.cluster_autoscalings,
            cluster_ipv4_cidr=self.cluster_ipv4_cidr,
            cluster_telemetries=self.cluster_telemetries,
            database_encryptions=self.database_encryptions,
            default_max_pods_per_node=self.default_max_pods_per_node,
            default_snat_statuses=self.default_snat_statuses,
            description=self.description,
            enable_binary_authorization=self.enable_binary_authorization,
            enable_intranode_visibility=self.enable_intranode_visibility,
            enable_kubernetes_alpha=self.enable_kubernetes_alpha,
            enable_legacy_abac=self.enable_legacy_abac,
            enable_shielded_nodes=self.enable_shielded_nodes,
            enable_tpu=self.enable_tpu,
            endpoint=self.endpoint,
            id=self.id,
            initial_node_count=self.initial_node_count,
            instance_group_urls=self.instance_group_urls,
            ip_allocation_policies=self.ip_allocation_policies,
            label_fingerprint=self.label_fingerprint,
            location=self.location,
            logging_service=self.logging_service,
            maintenance_policies=self.maintenance_policies,
            master_authorized_networks_configs=self.master_authorized_networks_configs,
            master_auths=self.master_auths,
            master_version=self.master_version,
            min_master_version=self.min_master_version,
            monitoring_service=self.monitoring_service,
            name=self.name,
            network=self.network,
            network_policies=self.network_policies,
            networking_mode=self.networking_mode,
            node_configs=self.node_configs,
            node_locations=self.node_locations,
            node_pools=self.node_pools,
            node_version=self.node_version,
            operation=self.operation,
            pod_security_policy_configs=self.pod_security_policy_configs,
            private_cluster_configs=self.private_cluster_configs,
            project=self.project,
            region=self.region,
            release_channels=self.release_channels,
            remove_default_node_pool=self.remove_default_node_pool,
            resource_labels=self.resource_labels,
            resource_usage_export_configs=self.resource_usage_export_configs,
            self_link=self.self_link,
            services_ipv4_cidr=self.services_ipv4_cidr,
            subnetwork=self.subnetwork,
            tpu_ipv4_cidr_block=self.tpu_ipv4_cidr_block,
            vertical_pod_autoscalings=self.vertical_pod_autoscalings,
            workload_identity_configs=self.workload_identity_configs,
            zone=self.zone)


def get_cluster(location: Optional[str] = None,
                name: Optional[str] = None,
                project: Optional[str] = None,
                region: Optional[str] = None,
                zone: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Get info about a GKE cluster from its name and location.


    :param str location: The location (zone or region) this cluster has been
           created in. One of `location`, `region`, `zone`, or a provider-level `zone` must
           be specified.
    :param str name: The name of the cluster.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The region this cluster has been created in. Deprecated
           in favour of `location`.
    :param str zone: The zone this cluster has been created in. Deprecated in
           favour of `location`.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:container/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        additional_zones=__ret__.additional_zones,
        addons_configs=__ret__.addons_configs,
        authenticator_groups_configs=__ret__.authenticator_groups_configs,
        cluster_autoscalings=__ret__.cluster_autoscalings,
        cluster_ipv4_cidr=__ret__.cluster_ipv4_cidr,
        cluster_telemetries=__ret__.cluster_telemetries,
        database_encryptions=__ret__.database_encryptions,
        default_max_pods_per_node=__ret__.default_max_pods_per_node,
        default_snat_statuses=__ret__.default_snat_statuses,
        description=__ret__.description,
        enable_binary_authorization=__ret__.enable_binary_authorization,
        enable_intranode_visibility=__ret__.enable_intranode_visibility,
        enable_kubernetes_alpha=__ret__.enable_kubernetes_alpha,
        enable_legacy_abac=__ret__.enable_legacy_abac,
        enable_shielded_nodes=__ret__.enable_shielded_nodes,
        enable_tpu=__ret__.enable_tpu,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        initial_node_count=__ret__.initial_node_count,
        instance_group_urls=__ret__.instance_group_urls,
        ip_allocation_policies=__ret__.ip_allocation_policies,
        label_fingerprint=__ret__.label_fingerprint,
        location=__ret__.location,
        logging_service=__ret__.logging_service,
        maintenance_policies=__ret__.maintenance_policies,
        master_authorized_networks_configs=__ret__.master_authorized_networks_configs,
        master_auths=__ret__.master_auths,
        master_version=__ret__.master_version,
        min_master_version=__ret__.min_master_version,
        monitoring_service=__ret__.monitoring_service,
        name=__ret__.name,
        network=__ret__.network,
        network_policies=__ret__.network_policies,
        networking_mode=__ret__.networking_mode,
        node_configs=__ret__.node_configs,
        node_locations=__ret__.node_locations,
        node_pools=__ret__.node_pools,
        node_version=__ret__.node_version,
        operation=__ret__.operation,
        pod_security_policy_configs=__ret__.pod_security_policy_configs,
        private_cluster_configs=__ret__.private_cluster_configs,
        project=__ret__.project,
        region=__ret__.region,
        release_channels=__ret__.release_channels,
        remove_default_node_pool=__ret__.remove_default_node_pool,
        resource_labels=__ret__.resource_labels,
        resource_usage_export_configs=__ret__.resource_usage_export_configs,
        self_link=__ret__.self_link,
        services_ipv4_cidr=__ret__.services_ipv4_cidr,
        subnetwork=__ret__.subnetwork,
        tpu_ipv4_cidr_block=__ret__.tpu_ipv4_cidr_block,
        vertical_pod_autoscalings=__ret__.vertical_pod_autoscalings,
        workload_identity_configs=__ret__.workload_identity_configs,
        zone=__ret__.zone)
