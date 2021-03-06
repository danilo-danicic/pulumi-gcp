// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./getGroupMemberships";
export * from "./getGroups";
export * from "./group";
export * from "./groupMembership";

// Import resources to register:
import { Group } from "./group";
import { GroupMembership } from "./groupMembership";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "gcp:cloudidentity/group:Group":
                return new Group(name, <any>undefined, { urn })
            case "gcp:cloudidentity/groupMembership:GroupMembership":
                return new GroupMembership(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("gcp", "cloudidentity/group", _module)
pulumi.runtime.registerResourceModule("gcp", "cloudidentity/groupMembership", _module)
