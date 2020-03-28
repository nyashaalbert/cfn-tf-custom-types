# Terraform::AWS::AlbListenerRule Action AuthenticateCognito

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationrequestextraparams" title="AuthenticationRequestExtraParams">AuthenticationRequestExtraParams</a>" : <i>[ <a href="action-authenticatecognito-authenticationrequestextraparams.md">AuthenticationRequestExtraParams</a>, ... ]</i>,
    "<a href="#onunauthenticatedrequest" title="OnUnauthenticatedRequest">OnUnauthenticatedRequest</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
    "<a href="#sessioncookiename" title="SessionCookieName">SessionCookieName</a>" : <i>String</i>,
    "<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>" : <i>Double</i>,
    "<a href="#userpoolarn" title="UserPoolArn">UserPoolArn</a>" : <i>String</i>,
    "<a href="#userpoolclientid" title="UserPoolClientId">UserPoolClientId</a>" : <i>String</i>,
    "<a href="#userpooldomain" title="UserPoolDomain">UserPoolDomain</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationrequestextraparams" title="AuthenticationRequestExtraParams">AuthenticationRequestExtraParams</a>: <i>
      - <a href="action-authenticatecognito-authenticationrequestextraparams.md">AuthenticationRequestExtraParams</a></i>
<a href="#onunauthenticatedrequest" title="OnUnauthenticatedRequest">OnUnauthenticatedRequest</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
<a href="#sessioncookiename" title="SessionCookieName">SessionCookieName</a>: <i>String</i>
<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>: <i>Double</i>
<a href="#userpoolarn" title="UserPoolArn">UserPoolArn</a>: <i>String</i>
<a href="#userpoolclientid" title="UserPoolClientId">UserPoolClientId</a>: <i>String</i>
<a href="#userpooldomain" title="UserPoolDomain">UserPoolDomain</a>: <i>String</i>
</pre>

## Properties

#### AuthenticationRequestExtraParams

_Required_: No

_Type_: List of <a href="action-authenticatecognito-authenticationrequestextraparams.md">AuthenticationRequestExtraParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnUnauthenticatedRequest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCookieName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolDomain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
