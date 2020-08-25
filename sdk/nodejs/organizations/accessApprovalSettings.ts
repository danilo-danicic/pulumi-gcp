// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class AccessApprovalSettings extends pulumi.CustomResource {
    /**
     * Get an existing AccessApprovalSettings resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccessApprovalSettingsState, opts?: pulumi.CustomResourceOptions): AccessApprovalSettings {
        return new AccessApprovalSettings(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:organizations/accessApprovalSettings:AccessApprovalSettings';

    /**
     * Returns true if the given object is an instance of AccessApprovalSettings.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessApprovalSettings {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessApprovalSettings.__pulumiType;
    }

    /**
     * This field will always be unset for the organization since organizations do not have ancestors.
     */
    public /*out*/ readonly enrolledAncestor!: pulumi.Output<boolean>;
    /**
     * A list of Google Cloud Services for which the given resource has Access Approval enrolled. Access requests for the
     * resource given by name against any of these services contained here will be required to have explicit approval.
     * Enrollment can be done for individual services. A maximum of 10 enrolled services will be enforced, to be expanded as
     * the set of supported services is expanded.
     */
    public readonly enrolledServices!: pulumi.Output<outputs.organizations.AccessApprovalSettingsEnrolledService[]>;
    /**
     * The resource name of the settings. Format is "organizations/{organization_id}/accessApprovalSettings"
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to
     * a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email
     * addresses are allowed.
     */
    public readonly notificationEmails!: pulumi.Output<string[]>;
    /**
     * ID of the organization of the access approval settings.
     */
    public readonly organizationId!: pulumi.Output<string>;

    /**
     * Create a AccessApprovalSettings resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessApprovalSettingsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AccessApprovalSettingsArgs | AccessApprovalSettingsState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AccessApprovalSettingsState | undefined;
            inputs["enrolledAncestor"] = state ? state.enrolledAncestor : undefined;
            inputs["enrolledServices"] = state ? state.enrolledServices : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["notificationEmails"] = state ? state.notificationEmails : undefined;
            inputs["organizationId"] = state ? state.organizationId : undefined;
        } else {
            const args = argsOrState as AccessApprovalSettingsArgs | undefined;
            if (!args || args.enrolledServices === undefined) {
                throw new Error("Missing required property 'enrolledServices'");
            }
            if (!args || args.organizationId === undefined) {
                throw new Error("Missing required property 'organizationId'");
            }
            inputs["enrolledServices"] = args ? args.enrolledServices : undefined;
            inputs["notificationEmails"] = args ? args.notificationEmails : undefined;
            inputs["organizationId"] = args ? args.organizationId : undefined;
            inputs["enrolledAncestor"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AccessApprovalSettings.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AccessApprovalSettings resources.
 */
export interface AccessApprovalSettingsState {
    /**
     * This field will always be unset for the organization since organizations do not have ancestors.
     */
    readonly enrolledAncestor?: pulumi.Input<boolean>;
    /**
     * A list of Google Cloud Services for which the given resource has Access Approval enrolled. Access requests for the
     * resource given by name against any of these services contained here will be required to have explicit approval.
     * Enrollment can be done for individual services. A maximum of 10 enrolled services will be enforced, to be expanded as
     * the set of supported services is expanded.
     */
    readonly enrolledServices?: pulumi.Input<pulumi.Input<inputs.organizations.AccessApprovalSettingsEnrolledService>[]>;
    /**
     * The resource name of the settings. Format is "organizations/{organization_id}/accessApprovalSettings"
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to
     * a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email
     * addresses are allowed.
     */
    readonly notificationEmails?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * ID of the organization of the access approval settings.
     */
    readonly organizationId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AccessApprovalSettings resource.
 */
export interface AccessApprovalSettingsArgs {
    /**
     * A list of Google Cloud Services for which the given resource has Access Approval enrolled. Access requests for the
     * resource given by name against any of these services contained here will be required to have explicit approval.
     * Enrollment can be done for individual services. A maximum of 10 enrolled services will be enforced, to be expanded as
     * the set of supported services is expanded.
     */
    readonly enrolledServices: pulumi.Input<pulumi.Input<inputs.organizations.AccessApprovalSettingsEnrolledService>[]>;
    /**
     * A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to
     * a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email
     * addresses are allowed.
     */
    readonly notificationEmails?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * ID of the organization of the access approval settings.
     */
    readonly organizationId: pulumi.Input<string>;
}
