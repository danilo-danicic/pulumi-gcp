// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class Project extends lumi.NamedResource implements ProjectArgs {
    public readonly billingAccount?: string;
    public readonly projectName?: string;
    public /*out*/ readonly number: string;
    public readonly orgId: string;
    public readonly projectId: string;
    public readonly skipDelete: boolean;

    constructor(name: string, args: ProjectArgs) {
        super(name);
        this.billingAccount = args.billingAccount;
        this.projectName = args.projectName;
        if (lumirt.defaultIfComputed(args.orgId, "") === undefined) {
            throw new Error("Property argument 'orgId' is required, but was missing");
        }
        this.orgId = args.orgId;
        if (lumirt.defaultIfComputed(args.projectId, "") === undefined) {
            throw new Error("Property argument 'projectId' is required, but was missing");
        }
        this.projectId = args.projectId;
        this.skipDelete = args.skipDelete;
    }
}

export interface ProjectArgs {
    readonly billingAccount?: string;
    readonly projectName?: string;
    readonly orgId: string;
    readonly projectId: string;
    readonly skipDelete?: boolean;
}
