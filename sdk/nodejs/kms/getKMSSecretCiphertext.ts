// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function getKMSSecretCiphertext(args: GetKMSSecretCiphertextArgs, opts?: pulumi.InvokeOptions): Promise<GetKMSSecretCiphertextResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("gcp:kms/getKMSSecretCiphertext:getKMSSecretCiphertext", {
        "cryptoKey": args.cryptoKey,
        "plaintext": args.plaintext,
    }, opts);
}

/**
 * A collection of arguments for invoking getKMSSecretCiphertext.
 */
export interface GetKMSSecretCiphertextArgs {
    /**
     * The id of the CryptoKey that will be used to
     * encrypt the provided plaintext. This is represented by the format
     * `{projectId}/{location}/{keyRingName}/{cryptoKeyName}`.
     */
    readonly cryptoKey: string;
    /**
     * The plaintext to be encrypted
     */
    readonly plaintext: string;
}

/**
 * A collection of values returned by getKMSSecretCiphertext.
 */
export interface GetKMSSecretCiphertextResult {
    /**
     * Contains the result of encrypting the provided plaintext, encoded in base64.
     */
    readonly ciphertext: string;
    readonly cryptoKey: string;
    readonly plaintext: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
