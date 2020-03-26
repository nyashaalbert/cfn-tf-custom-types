# Terraform::AWS::DatasyncTask

Manages an AWS DataSync Task, which represents a configuration for synchronization. Starting an execution of these DataSync Tasks (actually synchronizing files) is performed outside of this Terraform resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DatasyncTask",
    "Properties" : {
        "<a href="#cloudwatchloggrouparn" title="CloudwatchLogGroupArn">CloudwatchLogGroupArn</a>" : <i>String</i>,
        "<a href="#destinationlocationarn" title="DestinationLocationArn">DestinationLocationArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sourcelocationarn" title="SourceLocationArn">SourceLocationArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DatasyncTask
Properties:
    <a href="#cloudwatchloggrouparn" title="CloudwatchLogGroupArn">CloudwatchLogGroupArn</a>: <i>String</i>
    <a href="#destinationlocationarn" title="DestinationLocationArn">DestinationLocationArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sourcelocationarn" title="SourceLocationArn">SourceLocationArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CloudwatchLogGroupArn

Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationLocationArn

Amazon Resource Name (ARN) of destination DataSync Location.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the DataSync Task.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceLocationArn

Amazon Resource Name (ARN) of source DataSync Location.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value pairs of resource tags to assign to the DataSync Task.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="options.md">Options</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.
