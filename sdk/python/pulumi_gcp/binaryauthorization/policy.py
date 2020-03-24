# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Policy(pulumi.CustomResource):
    admission_whitelist_patterns: pulumi.Output[list]
    """
    A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
    image's admission requests will always be permitted regardless of your admission rules.

      * `namePattern` (`str`)
    """
    cluster_admission_rules: pulumi.Output[list]
    """
    Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
    must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
    denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
    location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').

      * `cluster` (`str`)
      * `enforcementMode` (`str`)
      * `evaluationMode` (`str`)
      * `requireAttestationsBies` (`list`)
    """
    default_admission_rule: pulumi.Output[dict]
    """
    Default admission rule for a cluster without a per-cluster admission rule.

      * `enforcementMode` (`str`)
      * `evaluationMode` (`str`)
      * `requireAttestationsBies` (`list`)
    """
    description: pulumi.Output[str]
    """
    A descriptive comment.
    """
    global_policy_evaluation_mode: pulumi.Output[str]
    """
    Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
    covered by the global policy will be subject to the project admission policy.
    """
    project: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, admission_whitelist_patterns=None, cluster_admission_rules=None, default_admission_rule=None, description=None, global_policy_evaluation_mode=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        A policy for container image binary authorization.


        To get more information about Policy, see:

        * [API documentation](https://cloud.google.com/binary-authorization/docs/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/binary-authorization/)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/binary_authorization_policy.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] admission_whitelist_patterns: A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
               image's admission requests will always be permitted regardless of your admission rules.
        :param pulumi.Input[list] cluster_admission_rules: Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
               must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
               denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
               location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
        :param pulumi.Input[dict] default_admission_rule: Default admission rule for a cluster without a per-cluster admission rule.
        :param pulumi.Input[str] description: A descriptive comment.
        :param pulumi.Input[str] global_policy_evaluation_mode: Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
               covered by the global policy will be subject to the project admission policy.

        The **admission_whitelist_patterns** object supports the following:

          * `namePattern` (`pulumi.Input[str]`)

        The **cluster_admission_rules** object supports the following:

          * `cluster` (`pulumi.Input[str]`)
          * `enforcementMode` (`pulumi.Input[str]`)
          * `evaluationMode` (`pulumi.Input[str]`)
          * `requireAttestationsBies` (`pulumi.Input[list]`)

        The **default_admission_rule** object supports the following:

          * `enforcementMode` (`pulumi.Input[str]`)
          * `evaluationMode` (`pulumi.Input[str]`)
          * `requireAttestationsBies` (`pulumi.Input[list]`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['admission_whitelist_patterns'] = admission_whitelist_patterns
            __props__['cluster_admission_rules'] = cluster_admission_rules
            if default_admission_rule is None:
                raise TypeError("Missing required property 'default_admission_rule'")
            __props__['default_admission_rule'] = default_admission_rule
            __props__['description'] = description
            __props__['global_policy_evaluation_mode'] = global_policy_evaluation_mode
            __props__['project'] = project
        super(Policy, __self__).__init__(
            'gcp:binaryauthorization/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, admission_whitelist_patterns=None, cluster_admission_rules=None, default_admission_rule=None, description=None, global_policy_evaluation_mode=None, project=None):
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] admission_whitelist_patterns: A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
               image's admission requests will always be permitted regardless of your admission rules.
        :param pulumi.Input[list] cluster_admission_rules: Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
               must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
               denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
               location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
        :param pulumi.Input[dict] default_admission_rule: Default admission rule for a cluster without a per-cluster admission rule.
        :param pulumi.Input[str] description: A descriptive comment.
        :param pulumi.Input[str] global_policy_evaluation_mode: Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
               covered by the global policy will be subject to the project admission policy.

        The **admission_whitelist_patterns** object supports the following:

          * `namePattern` (`pulumi.Input[str]`)

        The **cluster_admission_rules** object supports the following:

          * `cluster` (`pulumi.Input[str]`)
          * `enforcementMode` (`pulumi.Input[str]`)
          * `evaluationMode` (`pulumi.Input[str]`)
          * `requireAttestationsBies` (`pulumi.Input[list]`)

        The **default_admission_rule** object supports the following:

          * `enforcementMode` (`pulumi.Input[str]`)
          * `evaluationMode` (`pulumi.Input[str]`)
          * `requireAttestationsBies` (`pulumi.Input[list]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admission_whitelist_patterns"] = admission_whitelist_patterns
        __props__["cluster_admission_rules"] = cluster_admission_rules
        __props__["default_admission_rule"] = default_admission_rule
        __props__["description"] = description
        __props__["global_policy_evaluation_mode"] = global_policy_evaluation_mode
        __props__["project"] = project
        return Policy(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

