# Terraform::OpenTelekomCloud::CceClusterV3

Provides a cluster resource (CCE).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::CceClusterV3",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotations.md">Annotations</a>, ... ]</i>,
        "<a href="#authenticationmode" title="AuthenticationMode">AuthenticationMode</a>" : <i>String</i>,
        "<a href="#billingmode" title="BillingMode">BillingMode</a>" : <i>Double</i>,
        "<a href="#clustertype" title="ClusterType">ClusterType</a>" : <i>String</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#containernetworkcidr" title="ContainerNetworkCidr">ContainerNetworkCidr</a>" : <i>String</i>,
        "<a href="#containernetworktype" title="ContainerNetworkType">ContainerNetworkType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#eip" title="Eip">Eip</a>" : <i>String</i>,
        "<a href="#extendparam" title="ExtendParam">ExtendParam</a>" : <i>[ <a href="extendparam.md">ExtendParam</a>, ... ]</i>,
        "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
        "<a href="#highwaysubnetid" title="HighwaySubnetId">HighwaySubnetId</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#multiaz" title="MultiAz">MultiAz</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::CceClusterV3
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotations.md">Annotations</a></i>
    <a href="#authenticationmode" title="AuthenticationMode">AuthenticationMode</a>: <i>String</i>
    <a href="#billingmode" title="BillingMode">BillingMode</a>: <i>Double</i>
    <a href="#clustertype" title="ClusterType">ClusterType</a>: <i>String</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#containernetworkcidr" title="ContainerNetworkCidr">ContainerNetworkCidr</a>: <i>String</i>
    <a href="#containernetworktype" title="ContainerNetworkType">ContainerNetworkType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#eip" title="Eip">Eip</a>: <i>String</i>
    <a href="#extendparam" title="ExtendParam">ExtendParam</a>: <i>
      - <a href="extendparam.md">ExtendParam</a></i>
    <a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
    <a href="#highwaysubnetid" title="HighwaySubnetId">HighwaySubnetId</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#multiaz" title="MultiAz">MultiAz</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Annotations

Cluster annotation, key/value pair format. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: List of <a href="annotations.md">Annotations</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationMode

Authentication mode of the cluster, possible values are x509 and rbac. Defaults to x509.
Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingMode

Charging mode of the cluster, which is 0 (on demand). Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterType

Cluster Type, possible values are VirtualMachine and BareMetal. Changing this parameter will create a new cluster resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

For the cluster version, possible values are v1.9.2-r2 or v1.11.3-r1. Changing this parameter will create a new cluster resource.
[OTC-API](https://docs.otc.t-systems.com/en-us/api2/cce/cce_02_0236.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerNetworkCidr

Container network segment. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerNetworkType

Container network type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Cluster description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eip

EIP address of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendParam

Extended parameter. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: List of <a href="extendparam.md">ExtendParam</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorId

Cluster specifications. Changing this parameter will create a new cluster resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighwaySubnetId

The ID of the high speed network used to create bare metal nodes. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Cluster tag, key/value pair format. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiAz

Enable multiple AZs for the cluster, only when using HA flavors. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Cluster name. Changing this parameter will create a new cluster resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the subnet used to create the node. Changing this parameter will create a new cluster resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The ID of the VPC used to create the node. Changing this parameter will create a new cluster resource.

_Required_: Yes

_Type_: String

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

#### CertificateClusters

Returns the <code>CertificateClusters</code> value.

#### CertificateUsers

Returns the <code>CertificateUsers</code> value.

#### External

Returns the <code>External</code> value.

#### ExternalOtc

Returns the <code>ExternalOtc</code> value.

#### Id

Returns the <code>Id</code> value.

#### Internal

Returns the <code>Internal</code> value.

#### Status

Returns the <code>Status</code> value.
