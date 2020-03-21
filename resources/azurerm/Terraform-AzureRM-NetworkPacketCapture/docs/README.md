# Terraform::AzureRM::NetworkPacketCapture

CloudFormation equivalent of azurerm_network_packet_capture

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::NetworkPacketCapture",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#maximumbytesperpacket" title="MaximumBytesPerPacket">MaximumBytesPerPacket</a>" : <i>Double</i>,
        "<a href="#maximumbytespersession" title="MaximumBytesPerSession">MaximumBytesPerSession</a>" : <i>Double</i>,
        "<a href="#maximumcaptureduration" title="MaximumCaptureDuration">MaximumCaptureDuration</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkwatchername" title="NetworkWatcherName">NetworkWatcherName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>,
        "<a href="#storagelocation" title="StorageLocation">StorageLocation</a>" : <i>[ <a href="storagelocation.md">StorageLocation</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::NetworkPacketCapture
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#maximumbytesperpacket" title="MaximumBytesPerPacket">MaximumBytesPerPacket</a>: <i>Double</i>
    <a href="#maximumbytespersession" title="MaximumBytesPerSession">MaximumBytesPerSession</a>: <i>Double</i>
    <a href="#maximumcaptureduration" title="MaximumCaptureDuration">MaximumCaptureDuration</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkwatchername" title="NetworkWatcherName">NetworkWatcherName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
    <a href="#storagelocation" title="StorageLocation">StorageLocation</a>: <i>
      - <a href="storagelocation.md">StorageLocation</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBytesPerPacket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBytesPerSession

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumCaptureDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkWatcherName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageLocation

_Required_: No

_Type_: List of <a href="storagelocation.md">StorageLocation</a>

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
