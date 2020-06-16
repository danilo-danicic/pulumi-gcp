// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Healthcare.Outputs
{

    [OutputType]
    public sealed class FhirStoreStreamConfigBigqueryDestination
    {
        /// <summary>
        /// BigQuery URI to a dataset, up to 2000 characters long, in the format bq://projectId.bqDatasetId
        /// </summary>
        public readonly string DatasetUri;
        /// <summary>
        /// The configuration for the exported BigQuery schema.  Structure is documented below.
        /// </summary>
        public readonly Outputs.FhirStoreStreamConfigBigqueryDestinationSchemaConfig SchemaConfig;

        [OutputConstructor]
        private FhirStoreStreamConfigBigqueryDestination(
            string datasetUri,

            Outputs.FhirStoreStreamConfigBigqueryDestinationSchemaConfig schemaConfig)
        {
            DatasetUri = datasetUri;
            SchemaConfig = schemaConfig;
        }
    }
}
