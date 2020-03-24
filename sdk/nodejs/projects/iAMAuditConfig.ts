// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Four different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:
 * 
 * * `gcp.projects.IAMPolicy`: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.
 * * `gcp.projects.IAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.
 * * `gcp.projects.IAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.
 * * `gcp.projects.IAMAuditConfig`: Authoritative for a given service. Updates the IAM policy to enable audit logging for the given service.
 * 
 * 
 * > **Note:** `gcp.projects.IAMPolicy` **cannot** be used in conjunction with `gcp.projects.IAMBinding`, `gcp.projects.IAMMember`, or `gcp.projects.IAMAuditConfig` or they will fight over what your policy should be.
 * 
 * > **Note:** `gcp.projects.IAMBinding` resources **can be** used in conjunction with `gcp.projects.IAMMember` resources **only if** they do not grant privilege to the same role.
 * 
 * ## google\_project\_iam\_binding
 * 
 * > **Note:** If `role` is set to `roles/owner` and you don't specify a user or service account you have access to in `members`, you can lock yourself out of your project.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const project = new gcp.projects.IAMBinding("project", {
 *     members: ["user:jane@example.com"],
 *     project: "your-project-id",
 *     role: "roles/editor",
 * });
 * ```
 * 
 * With IAM Conditions:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const project = new gcp.projects.IAMBinding("project", {
 *     condition: {
 *         description: "Expiring at midnight of 2019-12-31",
 *         expression: "request.time < timestamp(\"2020-01-01T00:00:00Z\")",
 *         title: "expiresAfter20191231",
 *     },
 *     members: ["user:jane@example.com"],
 *     project: "your-project-id",
 *     role: "roles/editor",
 * });
 * ```
 * 
 * ## google\_project\_iam\_member
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const project = new gcp.projects.IAMMember("project", {
 *     member: "user:jane@example.com",
 *     project: "your-project-id",
 *     role: "roles/editor",
 * });
 * ```
 * 
 * With IAM Conditions:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const project = new gcp.projects.IAMMember("project", {
 *     condition: {
 *         description: "Expiring at midnight of 2019-12-31",
 *         expression: "request.time < timestamp(\"2020-01-01T00:00:00Z\")",
 *         title: "expiresAfter20191231",
 *     },
 *     member: "user:jane@example.com",
 *     project: "your-project-id",
 *     role: "roles/editor",
 * });
 * ```
 * 
 * ## google\_project\_iam\_audit\_config
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const project = new gcp.projects.IAMAuditConfig("project", {
 *     auditLogConfigs: [{
 *         exemptedMembers: ["user:joebloggs@hashicorp.com"],
 *         logType: "DATA_READ",
 *     }],
 *     project: "your-project-id",
 *     service: "allServices",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_project_iam.html.markdown.
 */
export class IAMAuditConfig extends pulumi.CustomResource {
    /**
     * Get an existing IAMAuditConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMAuditConfigState, opts?: pulumi.CustomResourceOptions): IAMAuditConfig {
        return new IAMAuditConfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:projects/iAMAuditConfig:IAMAuditConfig';

    /**
     * Returns true if the given object is an instance of IAMAuditConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IAMAuditConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IAMAuditConfig.__pulumiType;
    }

    /**
     * The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
     */
    public readonly auditLogConfigs!: pulumi.Output<outputs.projects.IAMAuditConfigAuditLogConfig[]>;
    /**
     * (Computed) The etag of the project's IAM policy.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * The project ID. If not specified for `gcp.projects.IAMBinding`, `gcp.projects.IAMMember`, or `gcp.projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
     * Required for `gcp.projects.IAMPolicy` - you must explicitly set the project, and it
     * will not be inferred from the provider.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_project\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `logTypes` specified in each `auditLogConfig` are enabled, and the `exemptedMembers` in each `auditLogConfig` are exempted.
     */
    public readonly service!: pulumi.Output<string>;

    /**
     * Create a IAMAuditConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IAMAuditConfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IAMAuditConfigArgs | IAMAuditConfigState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IAMAuditConfigState | undefined;
            inputs["auditLogConfigs"] = state ? state.auditLogConfigs : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["service"] = state ? state.service : undefined;
        } else {
            const args = argsOrState as IAMAuditConfigArgs | undefined;
            if (!args || args.auditLogConfigs === undefined) {
                throw new Error("Missing required property 'auditLogConfigs'");
            }
            if (!args || args.service === undefined) {
                throw new Error("Missing required property 'service'");
            }
            inputs["auditLogConfigs"] = args ? args.auditLogConfigs : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["service"] = args ? args.service : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(IAMAuditConfig.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IAMAuditConfig resources.
 */
export interface IAMAuditConfigState {
    /**
     * The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
     */
    readonly auditLogConfigs?: pulumi.Input<pulumi.Input<inputs.projects.IAMAuditConfigAuditLogConfig>[]>;
    /**
     * (Computed) The etag of the project's IAM policy.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * The project ID. If not specified for `gcp.projects.IAMBinding`, `gcp.projects.IAMMember`, or `gcp.projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
     * Required for `gcp.projects.IAMPolicy` - you must explicitly set the project, and it
     * will not be inferred from the provider.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_project\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `logTypes` specified in each `auditLogConfig` are enabled, and the `exemptedMembers` in each `auditLogConfig` are exempted.
     */
    readonly service?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IAMAuditConfig resource.
 */
export interface IAMAuditConfigArgs {
    /**
     * The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
     */
    readonly auditLogConfigs: pulumi.Input<pulumi.Input<inputs.projects.IAMAuditConfigAuditLogConfig>[]>;
    /**
     * The project ID. If not specified for `gcp.projects.IAMBinding`, `gcp.projects.IAMMember`, or `gcp.projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
     * Required for `gcp.projects.IAMPolicy` - you must explicitly set the project, and it
     * will not be inferred from the provider.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_project\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `logTypes` specified in each `auditLogConfig` are enabled, and the `exemptedMembers` in each `auditLogConfig` are exempted.
     */
    readonly service: pulumi.Input<string>;
}
