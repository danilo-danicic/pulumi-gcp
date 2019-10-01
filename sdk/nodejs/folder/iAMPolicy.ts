// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Allows creation and management of the IAM policy for an existing Google Cloud
 * Platform folder.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const department1 = new gcp.organizations.Folder("department1", {
 *     displayName: "Department 1",
 *     parent: "organizations/1234567",
 * });
 * const admin = gcp.organizations.getIAMPolicy({
 *     bindings: [{
 *         members: ["user:jane@example.com"],
 *         role: "roles/editor",
 *     }],
 * });
 * const folderAdminPolicy = new gcp.folder.IAMPolicy("folderAdminPolicy", {
 *     folder: department1.name,
 *     policyData: admin.policyData,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/folder_iam_policy.html.markdown.
 */
export class IAMPolicy extends pulumi.CustomResource {
    /**
     * Get an existing IAMPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMPolicyState, opts?: pulumi.CustomResourceOptions): IAMPolicy {
        return new IAMPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:folder/iAMPolicy:IAMPolicy';

    /**
     * Returns true if the given object is an instance of IAMPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IAMPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IAMPolicy.__pulumiType;
    }

    /**
     * (Computed) The etag of the folder's IAM policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
     */
    public readonly folder!: pulumi.Output<string>;
    /**
     * The `gcp.organizations.getIAMPolicy` data source that represents
     * the IAM policy that will be applied to the folder. This policy overrides any existing
     * policy applied to the folder.
     */
    public readonly policyData!: pulumi.Output<string>;

    /**
     * Create a IAMPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IAMPolicyArgs | IAMPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IAMPolicyState | undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["folder"] = state ? state.folder : undefined;
            inputs["policyData"] = state ? state.policyData : undefined;
        } else {
            const args = argsOrState as IAMPolicyArgs | undefined;
            if (!args || args.folder === undefined) {
                throw new Error("Missing required property 'folder'");
            }
            if (!args || args.policyData === undefined) {
                throw new Error("Missing required property 'policyData'");
            }
            inputs["folder"] = args ? args.folder : undefined;
            inputs["policyData"] = args ? args.policyData : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(IAMPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IAMPolicy resources.
 */
export interface IAMPolicyState {
    /**
     * (Computed) The etag of the folder's IAM policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
     */
    readonly folder?: pulumi.Input<string>;
    /**
     * The `gcp.organizations.getIAMPolicy` data source that represents
     * the IAM policy that will be applied to the folder. This policy overrides any existing
     * policy applied to the folder.
     */
    readonly policyData?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IAMPolicy resource.
 */
export interface IAMPolicyArgs {
    /**
     * The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
     */
    readonly folder: pulumi.Input<string>;
    /**
     * The `gcp.organizations.getIAMPolicy` data source that represents
     * the IAM policy that will be applied to the folder. This policy overrides any existing
     * policy applied to the folder.
     */
    readonly policyData: pulumi.Input<string>;
}
