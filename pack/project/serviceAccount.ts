// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class ServiceAccount extends lumi.NamedResource implements ServiceAccountArgs {
    public readonly accountId: string;
    public readonly displayName?: string;
    public /*out*/ readonly email: string;
    public /*out*/ readonly serviceAccountName: string;
    public readonly policyData?: string;
    public readonly project?: string;
    public /*out*/ readonly uniqueId: string;

    constructor(name: string, args: ServiceAccountArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.accountId, "") === undefined) {
            throw new Error("Property argument 'accountId' is required, but was missing");
        }
        this.accountId = args.accountId;
        this.displayName = args.displayName;
        this.policyData = args.policyData;
        this.project = args.project;
    }
}

export interface ServiceAccountArgs {
    readonly accountId: string;
    readonly displayName?: string;
    readonly policyData?: string;
    readonly project?: string;
}
