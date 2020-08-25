// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Replace all existing Access Levels in an Access Policy with the Access Levels provided. This is done atomically.
 * This is a bulk edit of all Access Levels and may override existing Access Levels created by `gcp.accesscontextmanager.AccessLevel`,
 * thus causing a permadiff if used alongside `gcp.accesscontextmanager.AccessLevel` on the same parent.
 *
 * To get more information about AccessLevels, see:
 *
 * * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)
 * * How-to Guides
 *     * [Access Policy Quickstart](https://cloud.google.com/access-context-manager/docs/quickstart)
 *
 * ## Example Usage
 */
export class AccessLevels extends pulumi.CustomResource {
    /**
     * Get an existing AccessLevels resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccessLevelsState, opts?: pulumi.CustomResourceOptions): AccessLevels {
        return new AccessLevels(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:accesscontextmanager/accessLevels:AccessLevels';

    /**
     * Returns true if the given object is an instance of AccessLevels.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessLevels {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessLevels.__pulumiType;
    }

    /**
     * The desired Access Levels that should replace all existing Access Levels in the Access Policy.
     * Structure is documented below.
     */
    public readonly accessLevels!: pulumi.Output<outputs.accesscontextmanager.AccessLevelsAccessLevel[] | undefined>;
    /**
     * The AccessPolicy this AccessLevel lives in.
     * Format: accessPolicies/{policy_id}
     */
    public readonly parent!: pulumi.Output<string>;

    /**
     * Create a AccessLevels resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessLevelsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AccessLevelsArgs | AccessLevelsState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AccessLevelsState | undefined;
            inputs["accessLevels"] = state ? state.accessLevels : undefined;
            inputs["parent"] = state ? state.parent : undefined;
        } else {
            const args = argsOrState as AccessLevelsArgs | undefined;
            if (!args || args.parent === undefined) {
                throw new Error("Missing required property 'parent'");
            }
            inputs["accessLevels"] = args ? args.accessLevels : undefined;
            inputs["parent"] = args ? args.parent : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AccessLevels.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AccessLevels resources.
 */
export interface AccessLevelsState {
    /**
     * The desired Access Levels that should replace all existing Access Levels in the Access Policy.
     * Structure is documented below.
     */
    readonly accessLevels?: pulumi.Input<pulumi.Input<inputs.accesscontextmanager.AccessLevelsAccessLevel>[]>;
    /**
     * The AccessPolicy this AccessLevel lives in.
     * Format: accessPolicies/{policy_id}
     */
    readonly parent?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AccessLevels resource.
 */
export interface AccessLevelsArgs {
    /**
     * The desired Access Levels that should replace all existing Access Levels in the Access Policy.
     * Structure is documented below.
     */
    readonly accessLevels?: pulumi.Input<pulumi.Input<inputs.accesscontextmanager.AccessLevelsAccessLevel>[]>;
    /**
     * The AccessPolicy this AccessLevel lives in.
     * Format: accessPolicies/{policy_id}
     */
    readonly parent: pulumi.Input<string>;
}
