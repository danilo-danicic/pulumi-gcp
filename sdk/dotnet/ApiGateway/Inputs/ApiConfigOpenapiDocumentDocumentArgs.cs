// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.ApiGateway.Inputs
{

    public sealed class ApiConfigOpenapiDocumentDocumentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Base64 encoded content of the file.
        /// </summary>
        [Input("contents", required: true)]
        public Input<string> Contents { get; set; } = null!;

        /// <summary>
        /// The file path (full or relative path). This is typically the path of the file when it is uploaded.
        /// </summary>
        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        public ApiConfigOpenapiDocumentDocumentArgs()
        {
        }
    }
}
