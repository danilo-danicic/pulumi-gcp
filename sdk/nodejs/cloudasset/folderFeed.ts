// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Describes a Cloud Asset Inventory feed used to to listen to asset updates.
 *
 * To get more information about FolderFeed, see:
 *
 * * [API documentation](https://cloud.google.com/asset-inventory/docs/reference/rest/)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/asset-inventory/docs)
 *
 * ## Example Usage
 */
export class FolderFeed extends pulumi.CustomResource {
    /**
     * Get an existing FolderFeed resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderFeedState, opts?: pulumi.CustomResourceOptions): FolderFeed {
        return new FolderFeed(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:cloudasset/folderFeed:FolderFeed';

    /**
     * Returns true if the given object is an instance of FolderFeed.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FolderFeed {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FolderFeed.__pulumiType;
    }

    /**
     * A list of the full names of the assets to receive updates. You must specify either or both of
     * assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
     * exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
     * See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
     */
    public readonly assetNames!: pulumi.Output<string[] | undefined>;
    /**
     * A list of types of the assets to receive updates. You must specify either or both of assetNames
     * and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
     * the feed. For example: "compute.googleapis.com/Disk"
     * See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
     * supported asset types.
     */
    public readonly assetTypes!: pulumi.Output<string[] | undefined>;
    /**
     * The project whose identity will be used when sending messages to the
     * destination pubsub topic. It also specifies the project for API
     * enablement check, quota, and billing.
     */
    public readonly billingProject!: pulumi.Output<string>;
    /**
     * A condition which determines whether an asset update should be published. If specified, an asset
     * will be returned only when the expression evaluates to true. When set, expression field
     * must be a valid CEL expression on a TemporalAsset with name temporal_asset. Example: a Feed with
     * expression "temporal_asset.deleted == true" will only publish Asset deletions. Other fields of
     * condition are optional.
     * Structure is documented below.
     */
    public readonly condition!: pulumi.Output<outputs.cloudasset.FolderFeedCondition | undefined>;
    /**
     * Asset content type. If not specified, no content but the asset name and type will be returned.
     * Possible values are `CONTENT_TYPE_UNSPECIFIED`, `RESOURCE`, `IAM_POLICY`, `ORG_POLICY`, and `ACCESS_POLICY`.
     */
    public readonly contentType!: pulumi.Output<string | undefined>;
    /**
     * This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
     */
    public readonly feedId!: pulumi.Output<string>;
    /**
     * Output configuration for asset feed destination.
     * Structure is documented below.
     */
    public readonly feedOutputConfig!: pulumi.Output<outputs.cloudasset.FolderFeedFeedOutputConfig>;
    /**
     * The folder this feed should be created in.
     */
    public readonly folder!: pulumi.Output<string>;
    /**
     * The ID of the folder where this feed has been created. Both [FOLDER_NUMBER] and folders/[FOLDER_NUMBER] are accepted.
     */
    public /*out*/ readonly folderId!: pulumi.Output<string>;
    /**
     * The format will be folders/{folder_number}/feeds/{client-assigned_feed_identifier}.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;

    /**
     * Create a FolderFeed resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FolderFeedArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FolderFeedArgs | FolderFeedState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FolderFeedState | undefined;
            inputs["assetNames"] = state ? state.assetNames : undefined;
            inputs["assetTypes"] = state ? state.assetTypes : undefined;
            inputs["billingProject"] = state ? state.billingProject : undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["contentType"] = state ? state.contentType : undefined;
            inputs["feedId"] = state ? state.feedId : undefined;
            inputs["feedOutputConfig"] = state ? state.feedOutputConfig : undefined;
            inputs["folder"] = state ? state.folder : undefined;
            inputs["folderId"] = state ? state.folderId : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as FolderFeedArgs | undefined;
            if (!args || args.billingProject === undefined) {
                throw new Error("Missing required property 'billingProject'");
            }
            if (!args || args.feedId === undefined) {
                throw new Error("Missing required property 'feedId'");
            }
            if (!args || args.feedOutputConfig === undefined) {
                throw new Error("Missing required property 'feedOutputConfig'");
            }
            if (!args || args.folder === undefined) {
                throw new Error("Missing required property 'folder'");
            }
            inputs["assetNames"] = args ? args.assetNames : undefined;
            inputs["assetTypes"] = args ? args.assetTypes : undefined;
            inputs["billingProject"] = args ? args.billingProject : undefined;
            inputs["condition"] = args ? args.condition : undefined;
            inputs["contentType"] = args ? args.contentType : undefined;
            inputs["feedId"] = args ? args.feedId : undefined;
            inputs["feedOutputConfig"] = args ? args.feedOutputConfig : undefined;
            inputs["folder"] = args ? args.folder : undefined;
            inputs["folderId"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(FolderFeed.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FolderFeed resources.
 */
export interface FolderFeedState {
    /**
     * A list of the full names of the assets to receive updates. You must specify either or both of
     * assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
     * exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
     * See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
     */
    readonly assetNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of types of the assets to receive updates. You must specify either or both of assetNames
     * and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
     * the feed. For example: "compute.googleapis.com/Disk"
     * See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
     * supported asset types.
     */
    readonly assetTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The project whose identity will be used when sending messages to the
     * destination pubsub topic. It also specifies the project for API
     * enablement check, quota, and billing.
     */
    readonly billingProject?: pulumi.Input<string>;
    /**
     * A condition which determines whether an asset update should be published. If specified, an asset
     * will be returned only when the expression evaluates to true. When set, expression field
     * must be a valid CEL expression on a TemporalAsset with name temporal_asset. Example: a Feed with
     * expression "temporal_asset.deleted == true" will only publish Asset deletions. Other fields of
     * condition are optional.
     * Structure is documented below.
     */
    readonly condition?: pulumi.Input<inputs.cloudasset.FolderFeedCondition>;
    /**
     * Asset content type. If not specified, no content but the asset name and type will be returned.
     * Possible values are `CONTENT_TYPE_UNSPECIFIED`, `RESOURCE`, `IAM_POLICY`, `ORG_POLICY`, and `ACCESS_POLICY`.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
     */
    readonly feedId?: pulumi.Input<string>;
    /**
     * Output configuration for asset feed destination.
     * Structure is documented below.
     */
    readonly feedOutputConfig?: pulumi.Input<inputs.cloudasset.FolderFeedFeedOutputConfig>;
    /**
     * The folder this feed should be created in.
     */
    readonly folder?: pulumi.Input<string>;
    /**
     * The ID of the folder where this feed has been created. Both [FOLDER_NUMBER] and folders/[FOLDER_NUMBER] are accepted.
     */
    readonly folderId?: pulumi.Input<string>;
    /**
     * The format will be folders/{folder_number}/feeds/{client-assigned_feed_identifier}.
     */
    readonly name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FolderFeed resource.
 */
export interface FolderFeedArgs {
    /**
     * A list of the full names of the assets to receive updates. You must specify either or both of
     * assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
     * exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
     * See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
     */
    readonly assetNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of types of the assets to receive updates. You must specify either or both of assetNames
     * and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
     * the feed. For example: "compute.googleapis.com/Disk"
     * See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
     * supported asset types.
     */
    readonly assetTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The project whose identity will be used when sending messages to the
     * destination pubsub topic. It also specifies the project for API
     * enablement check, quota, and billing.
     */
    readonly billingProject: pulumi.Input<string>;
    /**
     * A condition which determines whether an asset update should be published. If specified, an asset
     * will be returned only when the expression evaluates to true. When set, expression field
     * must be a valid CEL expression on a TemporalAsset with name temporal_asset. Example: a Feed with
     * expression "temporal_asset.deleted == true" will only publish Asset deletions. Other fields of
     * condition are optional.
     * Structure is documented below.
     */
    readonly condition?: pulumi.Input<inputs.cloudasset.FolderFeedCondition>;
    /**
     * Asset content type. If not specified, no content but the asset name and type will be returned.
     * Possible values are `CONTENT_TYPE_UNSPECIFIED`, `RESOURCE`, `IAM_POLICY`, `ORG_POLICY`, and `ACCESS_POLICY`.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
     */
    readonly feedId: pulumi.Input<string>;
    /**
     * Output configuration for asset feed destination.
     * Structure is documented below.
     */
    readonly feedOutputConfig: pulumi.Input<inputs.cloudasset.FolderFeedFeedOutputConfig>;
    /**
     * The folder this feed should be created in.
     */
    readonly folder: pulumi.Input<string>;
}
