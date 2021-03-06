// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./function";
export * from "./functionIamBinding";
export * from "./functionIamMember";
export * from "./functionIamPolicy";
export * from "./getFunction";
export * from "./zMixins";

// Import resources to register:
import { Function } from "./function";
import { FunctionIamBinding } from "./functionIamBinding";
import { FunctionIamMember } from "./functionIamMember";
import { FunctionIamPolicy } from "./functionIamPolicy";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "gcp:cloudfunctions/function:Function":
                return new Function(name, <any>undefined, { urn })
            case "gcp:cloudfunctions/functionIamBinding:FunctionIamBinding":
                return new FunctionIamBinding(name, <any>undefined, { urn })
            case "gcp:cloudfunctions/functionIamMember:FunctionIamMember":
                return new FunctionIamMember(name, <any>undefined, { urn })
            case "gcp:cloudfunctions/functionIamPolicy:FunctionIamPolicy":
                return new FunctionIamPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("gcp", "cloudfunctions/function", _module)
pulumi.runtime.registerResourceModule("gcp", "cloudfunctions/functionIamBinding", _module)
pulumi.runtime.registerResourceModule("gcp", "cloudfunctions/functionIamMember", _module)
pulumi.runtime.registerResourceModule("gcp", "cloudfunctions/functionIamPolicy", _module)
