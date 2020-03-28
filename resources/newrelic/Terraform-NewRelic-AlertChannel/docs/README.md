# Terraform::NewRelic::AlertChannel

Use this resource to create and manage New Relic alert policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::AlertChannel",
    "Properties" : {
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>[ <a href="configuration.md">Configuration</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::AlertChannel
Properties:
    <a href="#configuration" title="Configuration">Configuration</a>: <i>
      - <a href="configuration.md">Configuration</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
</pre>

## Properties

#### Configuration

**Deprecated** (Optional) A map of key/value pairs with channel type specific values. This argument is deprecated.  Use the `config` argument instead.

_Required_: No

_Type_: List of <a href="configuration.md">Configuration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the channel.
* `type` - (Required) The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
* `config` - (Optional) A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See [Nested config blocks](#nested-`config`-blocks) below for details.
* `configuration` - **Deprecated** (Optional) A map of key/value pairs with channel type specific values. This argument is deprecated.  Use the `config` argument instead.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
* `config` - (Optional) A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See [Nested config blocks](#nested-`config`-blocks) below for details.
* `configuration` - **Deprecated** (Optional) A map of key/value pairs with channel type specific values. This argument is deprecated.  Use the `config` argument instead.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.
