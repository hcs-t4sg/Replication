# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ChatStub(object):
    """The chat service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/greet.Chat/SendMessage',
                request_serializer=chat__pb2.MessageSendRequest.SerializeToString,
                response_deserializer=chat__pb2.MessageSendResponse.FromString,
                )
        self.ChatStream = channel.unary_stream(
                '/greet.Chat/ChatStream',
                request_serializer=chat__pb2.ChatRequest.SerializeToString,
                response_deserializer=chat__pb2.SingleMessage.FromString,
                )
        self.CreateAccount = channel.unary_unary(
                '/greet.Chat/CreateAccount',
                request_serializer=chat__pb2.CreateAccountRequest.SerializeToString,
                response_deserializer=chat__pb2.CreateAccountResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/greet.Chat/Login',
                request_serializer=chat__pb2.LoginRequest.SerializeToString,
                response_deserializer=chat__pb2.LoginResponse.FromString,
                )
        self.Logout = channel.unary_unary(
                '/greet.Chat/Logout',
                request_serializer=chat__pb2.LogoutRequest.SerializeToString,
                response_deserializer=chat__pb2.LogoutResponse.FromString,
                )
        self.ListAccounts = channel.unary_unary(
                '/greet.Chat/ListAccounts',
                request_serializer=chat__pb2.ListAccountsRequest.SerializeToString,
                response_deserializer=chat__pb2.ListAccountsResponse.FromString,
                )
        self.DeleteAccount = channel.unary_unary(
                '/greet.Chat/DeleteAccount',
                request_serializer=chat__pb2.DeleteAccountRequest.SerializeToString,
                response_deserializer=chat__pb2.DeleteAccountResponse.FromString,
                )
        self.GetServerId = channel.unary_unary(
                '/greet.Chat/GetServerId',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.GetServerIdResponse.FromString,
                )
        self.UpdatePrimaryServer = channel.unary_unary(
                '/greet.Chat/UpdatePrimaryServer',
                request_serializer=chat__pb2.UpdatePrimaryServerRequest.SerializeToString,
                response_deserializer=chat__pb2.UpdatePrimaryServerResponse.FromString,
                )


class ChatServicer(object):
    """The chat service definition.
    """

    def SendMessage(self, request, context):
        """Sends a message to a user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChatStream(self, request, context):
        """Open a stream of messages for a client; should never be called explicitly by user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAccount(self, request, context):
        """Creates a new account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Logs into an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Logs out of an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccounts(self, request, context):
        """Gets a list of accounts matching a wildcard
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAccount(self, request, context):
        """Deletes an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerId(self, request, context):
        """Gets server id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePrimaryServer(self, request, context):
        """Updates primary server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=chat__pb2.MessageSendRequest.FromString,
                    response_serializer=chat__pb2.MessageSendResponse.SerializeToString,
            ),
            'ChatStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ChatStream,
                    request_deserializer=chat__pb2.ChatRequest.FromString,
                    response_serializer=chat__pb2.SingleMessage.SerializeToString,
            ),
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=chat__pb2.CreateAccountRequest.FromString,
                    response_serializer=chat__pb2.CreateAccountResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=chat__pb2.LoginRequest.FromString,
                    response_serializer=chat__pb2.LoginResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=chat__pb2.LogoutRequest.FromString,
                    response_serializer=chat__pb2.LogoutResponse.SerializeToString,
            ),
            'ListAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccounts,
                    request_deserializer=chat__pb2.ListAccountsRequest.FromString,
                    response_serializer=chat__pb2.ListAccountsResponse.SerializeToString,
            ),
            'DeleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAccount,
                    request_deserializer=chat__pb2.DeleteAccountRequest.FromString,
                    response_serializer=chat__pb2.DeleteAccountResponse.SerializeToString,
            ),
            'GetServerId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerId,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.GetServerIdResponse.SerializeToString,
            ),
            'UpdatePrimaryServer': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePrimaryServer,
                    request_deserializer=chat__pb2.UpdatePrimaryServerRequest.FromString,
                    response_serializer=chat__pb2.UpdatePrimaryServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chat(object):
    """The chat service definition.
    """

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/SendMessage',
            chat__pb2.MessageSendRequest.SerializeToString,
            chat__pb2.MessageSendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChatStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greet.Chat/ChatStream',
            chat__pb2.ChatRequest.SerializeToString,
            chat__pb2.SingleMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/CreateAccount',
            chat__pb2.CreateAccountRequest.SerializeToString,
            chat__pb2.CreateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/Login',
            chat__pb2.LoginRequest.SerializeToString,
            chat__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/Logout',
            chat__pb2.LogoutRequest.SerializeToString,
            chat__pb2.LogoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/ListAccounts',
            chat__pb2.ListAccountsRequest.SerializeToString,
            chat__pb2.ListAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/DeleteAccount',
            chat__pb2.DeleteAccountRequest.SerializeToString,
            chat__pb2.DeleteAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/GetServerId',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.GetServerIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePrimaryServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Chat/UpdatePrimaryServer',
            chat__pb2.UpdatePrimaryServerRequest.SerializeToString,
            chat__pb2.UpdatePrimaryServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
