// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get information about a Google Billing Account.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const acct = pulumi.output(gcp.organizations.getBillingAccount({
 *     displayName: "My Billing Account",
 *     open: true,
 * }));
 * const myProject = new gcp.organizations.Project("my_project", {
 *     billingAccount: acct.id,
 *     orgId: "1234567",
 *     projectId: "your-project-id",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/billing_account.html.markdown.
 */
export function getBillingAccount(args?: GetBillingAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetBillingAccountResult> & GetBillingAccountResult {
    args = args || {};
    const promise: Promise<GetBillingAccountResult> = pulumi.runtime.invoke("gcp:organizations/getBillingAccount:getBillingAccount", {
        "billingAccount": args.billingAccount,
        "displayName": args.displayName,
        "open": args.open,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getBillingAccount.
 */
export interface GetBillingAccountArgs {
    /**
     * The name of the billing account in the form `{billing_account_id}` or `billingAccounts/{billing_account_id}`.
     */
    readonly billingAccount?: string;
    /**
     * The display name of the billing account.
     */
    readonly displayName?: string;
    /**
     * `true` if the billing account is open, `false` if the billing account is closed.
     */
    readonly open?: boolean;
}

/**
 * A collection of values returned by getBillingAccount.
 */
export interface GetBillingAccountResult {
    readonly billingAccount?: string;
    readonly displayName: string;
    /**
     * The resource name of the billing account in the form `billingAccounts/{billing_account_id}`.
     */
    readonly name: string;
    readonly open: boolean;
    /**
     * The IDs of any projects associated with the billing account.
     */
    readonly projectIds: string[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
