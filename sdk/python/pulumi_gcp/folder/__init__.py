# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .access_approval_settings import *
from .get_organization_policy import *
from .iam_audit_config import *
from .iam_binding import *
from .iam_member import *
from .iam_policy import *
from .organization_policy import *
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
            if typ == "gcp:folder/accessApprovalSettings:AccessApprovalSettings":
                return AccessApprovalSettings(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:folder/iAMBinding:IAMBinding":
                return IAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:folder/iAMMember:IAMMember":
                return IAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:folder/iAMPolicy:IAMPolicy":
                return IAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:folder/iamAuditConfig:IamAuditConfig":
                return IamAuditConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:folder/organizationPolicy:OrganizationPolicy":
                return OrganizationPolicy(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp", "folder/accessApprovalSettings", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "folder/iAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "folder/iAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "folder/iAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "folder/iamAuditConfig", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "folder/organizationPolicy", _module_instance)

_register_module()
