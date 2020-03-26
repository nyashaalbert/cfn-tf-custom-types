# Terraform::OpsGenie::NotificationPolicy AutoRestartAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxrepeatcount" title="MaxRepeatCount">MaxRepeatCount</a>" : <i>Double</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>[ <a href="autorestartaction-duration.md">Duration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxrepeatcount" title="MaxRepeatCount">MaxRepeatCount</a>: <i>Double</i>
<a href="#duration" title="Duration">Duration</a>: <i>
      - <a href="autorestartaction-duration.md">Duration</a></i>
</pre>

## Properties

#### MaxRepeatCount

How many times to repeat. This is a integer attribute.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: List of <a href="autorestartaction-duration.md">Duration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
