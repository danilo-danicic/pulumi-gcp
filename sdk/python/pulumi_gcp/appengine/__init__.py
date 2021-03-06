# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .application import *
from .application_url_dispatch_rules import *
from .domain_mapping import *
from .engine_split_traffic import *
from .firewall_rule import *
from .flexible_app_version import *
from .get_default_service_account import *
from .standard_app_version import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp:appengine/application:Application":
                return Application(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:appengine/applicationUrlDispatchRules:ApplicationUrlDispatchRules":
                return ApplicationUrlDispatchRules(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:appengine/domainMapping:DomainMapping":
                return DomainMapping(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:appengine/engineSplitTraffic:EngineSplitTraffic":
                return EngineSplitTraffic(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:appengine/firewallRule:FirewallRule":
                return FirewallRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:appengine/flexibleAppVersion:FlexibleAppVersion":
                return FlexibleAppVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:appengine/standardAppVersion:StandardAppVersion":
                return StandardAppVersion(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp", "appengine/application", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "appengine/applicationUrlDispatchRules", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "appengine/domainMapping", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "appengine/engineSplitTraffic", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "appengine/firewallRule", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "appengine/flexibleAppVersion", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "appengine/standardAppVersion", _module_instance)

_register_module()
