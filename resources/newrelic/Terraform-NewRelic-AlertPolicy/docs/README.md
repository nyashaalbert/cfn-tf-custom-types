# Terraform::NewRelic::AlertPolicy

CloudFormation equivalent of newrelic_alert_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::AlertPolicy",
    "Properties" : {
        "<a href="#channelids" title="ChannelIds">ChannelIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#incidentpreference" title="IncidentPreference">IncidentPreference</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::AlertPolicy
Properties:
    <a href="#channelids" title="ChannelIds">ChannelIds</a>: <i>
      - Double</i>
    <a href="#incidentpreference" title="IncidentPreference">IncidentPreference</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ChannelIds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentPreference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.
