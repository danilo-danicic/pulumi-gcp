// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Get the IP address from a static address reserved for a Global Forwarding Rule which are only used for HTTP load balancing. For more information see
 * the official [API](https://cloud.google.com/compute/docs/reference/latest/globalAddresses) documentation.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const myAddress = pulumi.output(gcp.compute.getGlobalAddress({
 *     name: "foobar",
 * }));
 * const prod = new gcp.dns.ManagedZone("prod", {
 *     dnsName: "prod.mydomain.com.",
 * });
 * const frontend = new gcp.dns.RecordSet("frontend", {
 *     managedZone: prod.name,
 *     rrdatas: [myAddress.address],
 *     ttl: 300,
 *     type: "A",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_global_address.html.markdown.
 */
export function getGlobalAddress(args: GetGlobalAddressArgs, opts?: pulumi.InvokeOptions): Promise<GetGlobalAddressResult> & GetGlobalAddressResult {
    const promise: Promise<GetGlobalAddressResult> = pulumi.runtime.invoke("gcp:compute/getGlobalAddress:getGlobalAddress", {
        "name": args.name,
        "project": args.project,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getGlobalAddress.
 */
export interface GetGlobalAddressArgs {
    /**
     * A unique name for the resource, required by GCE.
     */
    readonly name: string;
    /**
     * The project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: string;
}

/**
 * A collection of values returned by getGlobalAddress.
 */
export interface GetGlobalAddressResult {
    /**
     * The IP of the created resource.
     */
    readonly address: string;
    readonly name: string;
    readonly project: string;
    /**
     * The URI of the created resource.
     */
    readonly selfLink: string;
    /**
     * Indicates if the address is used. Possible values are: RESERVED or IN_USE.
     */
    readonly status: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
