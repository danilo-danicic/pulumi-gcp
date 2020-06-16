// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataCatalog
{
    /// <summary>
    /// Tags are used to attach custom metadata to Data Catalog resources. Tags conform to the specifications within their tag template.
    /// 
    /// See [Data Catalog IAM](https://cloud.google.com/data-catalog/docs/concepts/iam) for information on the permissions needed to create or view tags.
    /// 
    /// 
    /// To get more information about Tag, see:
    /// 
    /// * [API documentation](https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.tags)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/data-catalog/docs)
    /// 
    /// ## Example Usage
    /// 
    /// ### Data Catalog Entry Tag Basic
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var entryGroup = new Gcp.DataCatalog.EntryGroup("entryGroup", new Gcp.DataCatalog.EntryGroupArgs
    ///         {
    ///             EntryGroupId = "my_entry_group",
    ///         });
    ///         var entry = new Gcp.DataCatalog.Entry("entry", new Gcp.DataCatalog.EntryArgs
    ///         {
    ///             EntryGroup = entryGroup.Id,
    ///             EntryId = "my_entry",
    ///             UserSpecifiedType = "my_custom_type",
    ///             UserSpecifiedSystem = "SomethingExternal",
    ///         });
    ///         var tagTemplate = new Gcp.DataCatalog.TagTemplate("tagTemplate", new Gcp.DataCatalog.TagTemplateArgs
    ///         {
    ///             TagTemplateId = "my_template",
    ///             Region = "us-central1",
    ///             DisplayName = "Demo Tag Template",
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "source",
    ///                     DisplayName = "Source of data asset",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         PrimitiveType = "STRING",
    ///                     },
    ///                     IsRequired = true,
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "num_rows",
    ///                     DisplayName = "Number of rows in the data asset",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         PrimitiveType = "DOUBLE",
    ///                     },
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "pii_type",
    ///                     DisplayName = "PII type",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         Enum_type = 
    ///                         {
    ///                             { "allowed_values", 
    ///                             {
    ///                                 
    ///                                 {
    ///                                     { "displayName", "EMAIL" },
    ///                                 },
    ///                                 
    ///                                 {
    ///                                     { "displayName", "SOCIAL SECURITY NUMBER" },
    ///                                 },
    ///                                 
    ///                                 {
    ///                                     { "displayName", "NONE" },
    ///                                 },
    ///                             } },
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///             ForceDelete = false,
    ///         });
    ///         var basicTag = new Gcp.DataCatalog.Tag("basicTag", new Gcp.DataCatalog.TagArgs
    ///         {
    ///             Parent = entry.Id,
    ///             Template = tagTemplate.Id,
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "source",
    ///                     StringValue = "my-string",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ### Data Catalog Entry Group Tag
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var entryGroup = new Gcp.DataCatalog.EntryGroup("entryGroup", new Gcp.DataCatalog.EntryGroupArgs
    ///         {
    ///             EntryGroupId = "my_entry_group",
    ///         });
    ///         var firstEntry = new Gcp.DataCatalog.Entry("firstEntry", new Gcp.DataCatalog.EntryArgs
    ///         {
    ///             EntryGroup = entryGroup.Id,
    ///             EntryId = "first_entry",
    ///             UserSpecifiedType = "my_custom_type",
    ///             UserSpecifiedSystem = "SomethingExternal",
    ///         });
    ///         var secondEntry = new Gcp.DataCatalog.Entry("secondEntry", new Gcp.DataCatalog.EntryArgs
    ///         {
    ///             EntryGroup = entryGroup.Id,
    ///             EntryId = "second_entry",
    ///             UserSpecifiedType = "another_custom_type",
    ///             UserSpecifiedSystem = "SomethingElseExternal",
    ///         });
    ///         var tagTemplate = new Gcp.DataCatalog.TagTemplate("tagTemplate", new Gcp.DataCatalog.TagTemplateArgs
    ///         {
    ///             TagTemplateId = "my_template",
    ///             Region = "us-central1",
    ///             DisplayName = "Demo Tag Template",
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "source",
    ///                     DisplayName = "Source of data asset",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         PrimitiveType = "STRING",
    ///                     },
    ///                     IsRequired = true,
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "num_rows",
    ///                     DisplayName = "Number of rows in the data asset",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         PrimitiveType = "DOUBLE",
    ///                     },
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "pii_type",
    ///                     DisplayName = "PII type",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         Enum_type = 
    ///                         {
    ///                             { "allowed_values", 
    ///                             {
    ///                                 
    ///                                 {
    ///                                     { "displayName", "EMAIL" },
    ///                                 },
    ///                                 
    ///                                 {
    ///                                     { "displayName", "SOCIAL SECURITY NUMBER" },
    ///                                 },
    ///                                 
    ///                                 {
    ///                                     { "displayName", "NONE" },
    ///                                 },
    ///                             } },
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///             ForceDelete = false,
    ///         });
    ///         var entryGroupTag = new Gcp.DataCatalog.Tag("entryGroupTag", new Gcp.DataCatalog.TagArgs
    ///         {
    ///             Parent = entryGroup.Id,
    ///             Template = tagTemplate.Id,
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "source",
    ///                     StringValue = "my-string",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ### Data Catalog Entry Tag Full
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var entryGroup = new Gcp.DataCatalog.EntryGroup("entryGroup", new Gcp.DataCatalog.EntryGroupArgs
    ///         {
    ///             EntryGroupId = "my_entry_group",
    ///         });
    ///         var entry = new Gcp.DataCatalog.Entry("entry", new Gcp.DataCatalog.EntryArgs
    ///         {
    ///             EntryGroup = entryGroup.Id,
    ///             EntryId = "my_entry",
    ///             UserSpecifiedType = "my_custom_type",
    ///             UserSpecifiedSystem = "SomethingExternal",
    ///             Schema = @"{
    ///   ""columns"": [
    ///     {
    ///       ""column"": ""first_name"",
    ///       ""description"": ""First name"",
    ///       ""mode"": ""REQUIRED"",
    ///       ""type"": ""STRING""
    ///     },
    ///     {
    ///       ""column"": ""last_name"",
    ///       ""description"": ""Last name"",
    ///       ""mode"": ""REQUIRED"",
    ///       ""type"": ""STRING""
    ///     },
    ///     {
    ///       ""column"": ""address"",
    ///       ""description"": ""Address"",
    ///       ""mode"": ""REPEATED"",
    ///       ""subcolumns"": [
    ///         {
    ///           ""column"": ""city"",
    ///           ""description"": ""City"",
    ///           ""mode"": ""NULLABLE"",
    ///           ""type"": ""STRING""
    ///         },
    ///         {
    ///           ""column"": ""state"",
    ///           ""description"": ""State"",
    ///           ""mode"": ""NULLABLE"",
    ///           ""type"": ""STRING""
    ///         }
    ///       ],
    ///       ""type"": ""RECORD""
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///         var tagTemplate = new Gcp.DataCatalog.TagTemplate("tagTemplate", new Gcp.DataCatalog.TagTemplateArgs
    ///         {
    ///             TagTemplateId = "my_template",
    ///             Region = "us-central1",
    ///             DisplayName = "Demo Tag Template",
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "source",
    ///                     DisplayName = "Source of data asset",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         PrimitiveType = "STRING",
    ///                     },
    ///                     IsRequired = true,
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "num_rows",
    ///                     DisplayName = "Number of rows in the data asset",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         PrimitiveType = "DOUBLE",
    ///                     },
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagTemplateFieldArgs
    ///                 {
    ///                     FieldId = "pii_type",
    ///                     DisplayName = "PII type",
    ///                     Type = new Gcp.DataCatalog.Inputs.TagTemplateFieldTypeArgs
    ///                     {
    ///                         Enum_type = 
    ///                         {
    ///                             { "allowed_values", 
    ///                             {
    ///                                 
    ///                                 {
    ///                                     { "displayName", "EMAIL" },
    ///                                 },
    ///                                 
    ///                                 {
    ///                                     { "displayName", "SOCIAL SECURITY NUMBER" },
    ///                                 },
    ///                                 
    ///                                 {
    ///                                     { "displayName", "NONE" },
    ///                                 },
    ///                             } },
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///             ForceDelete = false,
    ///         });
    ///         var basicTag = new Gcp.DataCatalog.Tag("basicTag", new Gcp.DataCatalog.TagArgs
    ///         {
    ///             Parent = entry.Id,
    ///             Template = tagTemplate.Id,
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "source",
    ///                     StringValue = "my-string",
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "num_rows",
    ///                     DoubleValue = 5,
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "pii_type",
    ///                     EnumValue = "EMAIL",
    ///                 },
    ///             },
    ///             Column = "address",
    ///         });
    ///         var second_tag = new Gcp.DataCatalog.Tag("second-tag", new Gcp.DataCatalog.TagArgs
    ///         {
    ///             Parent = entry.Id,
    ///             Template = tagTemplate.Id,
    ///             Fields = 
    ///             {
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "source",
    ///                     StringValue = "my-string",
    ///                 },
    ///                 new Gcp.DataCatalog.Inputs.TagFieldArgs
    ///                 {
    ///                     FieldName = "pii_type",
    ///                     EnumValue = "NONE",
    ///                 },
    ///             },
    ///             Column = "first_name",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Tag : Pulumi.CustomResource
    {
        /// <summary>
        /// Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an
        /// individual column based on that schema.
        /// For attaching a tag to a nested column, use `.` to separate the column names. Example:
        /// `outer_column.inner_column`
        /// </summary>
        [Output("column")]
        public Output<string?> Column { get; private set; } = null!;

        /// <summary>
        /// This maps the ID of a tag field to the value of and additional information about that field.
        /// Valid field IDs are defined by the tag's template. A tag must have at least 1 field and at most 500 fields.  Structure is documented below.
        /// </summary>
        [Output("fields")]
        public Output<ImmutableArray<Outputs.TagField>> Fields { get; private set; } = null!;

        /// <summary>
        /// The resource name of the tag in URL format. Example:
        /// projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}/tags/{tag_id} or
        /// projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/tags/{tag_id} where tag_id is a system-generated
        /// identifier. Note that this Tag may not actually be stored in the location in this name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the parent this tag is attached to. This can be the name of an entry or an entry group. If an entry group, the tag will be attached to
        /// all entries in that group.
        /// </summary>
        [Output("parent")]
        public Output<string?> Parent { get; private set; } = null!;

        /// <summary>
        /// The resource name of the tag template that this tag uses. Example:
        /// projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
        /// This field cannot be modified after creation.
        /// </summary>
        [Output("template")]
        public Output<string> Template { get; private set; } = null!;

        /// <summary>
        /// The display name of the tag template.
        /// </summary>
        [Output("templateDisplayname")]
        public Output<string> TemplateDisplayname { get; private set; } = null!;


        /// <summary>
        /// Create a Tag resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Tag(string name, TagArgs args, CustomResourceOptions? options = null)
            : base("gcp:datacatalog/tag:Tag", name, args ?? new TagArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Tag(string name, Input<string> id, TagState? state = null, CustomResourceOptions? options = null)
            : base("gcp:datacatalog/tag:Tag", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Tag resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Tag Get(string name, Input<string> id, TagState? state = null, CustomResourceOptions? options = null)
        {
            return new Tag(name, id, state, options);
        }
    }

    public sealed class TagArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an
        /// individual column based on that schema.
        /// For attaching a tag to a nested column, use `.` to separate the column names. Example:
        /// `outer_column.inner_column`
        /// </summary>
        [Input("column")]
        public Input<string>? Column { get; set; }

        [Input("fields", required: true)]
        private InputList<Inputs.TagFieldArgs>? _fields;

        /// <summary>
        /// This maps the ID of a tag field to the value of and additional information about that field.
        /// Valid field IDs are defined by the tag's template. A tag must have at least 1 field and at most 500 fields.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.TagFieldArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.TagFieldArgs>());
            set => _fields = value;
        }

        /// <summary>
        /// The name of the parent this tag is attached to. This can be the name of an entry or an entry group. If an entry group, the tag will be attached to
        /// all entries in that group.
        /// </summary>
        [Input("parent")]
        public Input<string>? Parent { get; set; }

        /// <summary>
        /// The resource name of the tag template that this tag uses. Example:
        /// projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
        /// This field cannot be modified after creation.
        /// </summary>
        [Input("template", required: true)]
        public Input<string> Template { get; set; } = null!;

        public TagArgs()
        {
        }
    }

    public sealed class TagState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an
        /// individual column based on that schema.
        /// For attaching a tag to a nested column, use `.` to separate the column names. Example:
        /// `outer_column.inner_column`
        /// </summary>
        [Input("column")]
        public Input<string>? Column { get; set; }

        [Input("fields")]
        private InputList<Inputs.TagFieldGetArgs>? _fields;

        /// <summary>
        /// This maps the ID of a tag field to the value of and additional information about that field.
        /// Valid field IDs are defined by the tag's template. A tag must have at least 1 field and at most 500 fields.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.TagFieldGetArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.TagFieldGetArgs>());
            set => _fields = value;
        }

        /// <summary>
        /// The resource name of the tag in URL format. Example:
        /// projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}/tags/{tag_id} or
        /// projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/tags/{tag_id} where tag_id is a system-generated
        /// identifier. Note that this Tag may not actually be stored in the location in this name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the parent this tag is attached to. This can be the name of an entry or an entry group. If an entry group, the tag will be attached to
        /// all entries in that group.
        /// </summary>
        [Input("parent")]
        public Input<string>? Parent { get; set; }

        /// <summary>
        /// The resource name of the tag template that this tag uses. Example:
        /// projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
        /// This field cannot be modified after creation.
        /// </summary>
        [Input("template")]
        public Input<string>? Template { get; set; }

        /// <summary>
        /// The display name of the tag template.
        /// </summary>
        [Input("templateDisplayname")]
        public Input<string>? TemplateDisplayname { get; set; }

        public TagState()
        {
        }
    }
}
