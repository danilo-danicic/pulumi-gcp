// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./gcpolicy";
export * from "./instance";
export * from "./instanceIamBinding";
export * from "./instanceIamMember";
export * from "./instanceIamPolicy";
export * from "./table";
export * from "./tableIamBinding";
export * from "./tableIamMember";
export * from "./tableIamPolicy";

// Import resources to register:
import { GCPolicy } from "./gcpolicy";
import { Instance } from "./instance";
import { InstanceIamBinding } from "./instanceIamBinding";
import { InstanceIamMember } from "./instanceIamMember";
import { InstanceIamPolicy } from "./instanceIamPolicy";
import { Table } from "./table";
import { TableIamBinding } from "./tableIamBinding";
import { TableIamMember } from "./tableIamMember";
import { TableIamPolicy } from "./tableIamPolicy";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "gcp:bigtable/gCPolicy:GCPolicy":
                return new GCPolicy(name, <any>undefined, { urn })
            case "gcp:bigtable/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "gcp:bigtable/instanceIamBinding:InstanceIamBinding":
                return new InstanceIamBinding(name, <any>undefined, { urn })
            case "gcp:bigtable/instanceIamMember:InstanceIamMember":
                return new InstanceIamMember(name, <any>undefined, { urn })
            case "gcp:bigtable/instanceIamPolicy:InstanceIamPolicy":
                return new InstanceIamPolicy(name, <any>undefined, { urn })
            case "gcp:bigtable/table:Table":
                return new Table(name, <any>undefined, { urn })
            case "gcp:bigtable/tableIamBinding:TableIamBinding":
                return new TableIamBinding(name, <any>undefined, { urn })
            case "gcp:bigtable/tableIamMember:TableIamMember":
                return new TableIamMember(name, <any>undefined, { urn })
            case "gcp:bigtable/tableIamPolicy:TableIamPolicy":
                return new TableIamPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("gcp", "bigtable/gCPolicy", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/instance", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/instanceIamBinding", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/instanceIamMember", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/instanceIamPolicy", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/table", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/tableIamBinding", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/tableIamMember", _module)
pulumi.runtime.registerResourceModule("gcp", "bigtable/tableIamPolicy", _module)
