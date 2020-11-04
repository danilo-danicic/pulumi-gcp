// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class ApiConfigIamMember extends pulumi.CustomResource {
    /**
     * Get an existing ApiConfigIamMember resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApiConfigIamMemberState, opts?: pulumi.CustomResourceOptions): ApiConfigIamMember {
        return new ApiConfigIamMember(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:apigateway/apiConfigIamMember:ApiConfigIamMember';

    /**
     * Returns true if the given object is an instance of ApiConfigIamMember.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiConfigIamMember {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiConfigIamMember.__pulumiType;
    }

    /**
     * The API to attach the config to.
     * Used to find the parent resource to bind the IAM policy to
     */
    public readonly api!: pulumi.Output<string>;
    public readonly apiConfig!: pulumi.Output<string>;
    public readonly condition!: pulumi.Output<outputs.apigateway.ApiConfigIamMemberCondition | undefined>;
    /**
     * (Computed) The etag of the IAM policy.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    public readonly member!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.apigateway.ApiConfigIamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    public readonly role!: pulumi.Output<string>;

    /**
     * Create a ApiConfigIamMember resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApiConfigIamMemberArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApiConfigIamMemberArgs | ApiConfigIamMemberState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ApiConfigIamMemberState | undefined;
            inputs["api"] = state ? state.api : undefined;
            inputs["apiConfig"] = state ? state.apiConfig : undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["member"] = state ? state.member : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as ApiConfigIamMemberArgs | undefined;
            if (!args || args.api === undefined) {
                throw new Error("Missing required property 'api'");
            }
            if (!args || args.apiConfig === undefined) {
                throw new Error("Missing required property 'apiConfig'");
            }
            if (!args || args.member === undefined) {
                throw new Error("Missing required property 'member'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["api"] = args ? args.api : undefined;
            inputs["apiConfig"] = args ? args.apiConfig : undefined;
            inputs["condition"] = args ? args.condition : undefined;
            inputs["member"] = args ? args.member : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ApiConfigIamMember.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApiConfigIamMember resources.
 */
export interface ApiConfigIamMemberState {
    /**
     * The API to attach the config to.
     * Used to find the parent resource to bind the IAM policy to
     */
    readonly api?: pulumi.Input<string>;
    readonly apiConfig?: pulumi.Input<string>;
    readonly condition?: pulumi.Input<inputs.apigateway.ApiConfigIamMemberCondition>;
    /**
     * (Computed) The etag of the IAM policy.
     */
    readonly etag?: pulumi.Input<string>;
    readonly member?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.apigateway.ApiConfigIamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    readonly role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApiConfigIamMember resource.
 */
export interface ApiConfigIamMemberArgs {
    /**
     * The API to attach the config to.
     * Used to find the parent resource to bind the IAM policy to
     */
    readonly api: pulumi.Input<string>;
    readonly apiConfig: pulumi.Input<string>;
    readonly condition?: pulumi.Input<inputs.apigateway.ApiConfigIamMemberCondition>;
    readonly member: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.apigateway.ApiConfigIamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    readonly role: pulumi.Input<string>;
}
