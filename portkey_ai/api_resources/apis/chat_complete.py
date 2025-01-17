from __future__ import annotations

import json
from typing import Mapping, Optional, Union, overload, Literal, List
from portkey_ai.api_resources.base_client import APIClient, AsyncAPIClient
from portkey_ai.api_resources.utils import (
    PortkeyApiPaths,
    Message,
    ChatCompletionChunk,
    ChatCompletions,
)

from portkey_ai.api_resources.streaming import AsyncStream, Stream
from portkey_ai.api_resources.apis.api_resource import APIResource, AsyncAPIResource


__all__ = ["ChatCompletion", "AsyncChatCompletion"]


class ChatCompletion(APIResource):
    completions: Completions

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self.completions = Completions(client)


class AsyncChatCompletion(AsyncAPIResource):
    completions: AsyncCompletions

    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client)
        self.completions = AsyncCompletions(client)


class Completions(APIResource):
    def __init__(self, client: APIClient) -> None:
        super().__init__(client)

    @overload
    def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        config: Optional[Union[Mapping, str]] = None,
        stream: Literal[True],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> Stream[ChatCompletionChunk]:
        ...

    @overload
    def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        config: Optional[Union[Mapping, str]] = None,
        stream: Literal[False] = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> ChatCompletions:
        ...

    @overload
    def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        config: Optional[Union[Mapping, str]] = None,
        stream: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> Union[ChatCompletions, Stream[ChatCompletionChunk]]:
        ...

    def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        stream: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> Union[ChatCompletions, Stream[ChatCompletionChunk]]:
        body = dict(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_k=top_k,
            top_p=top_p,
            stream=stream,
            **kwargs,
        )

        return self._post(
            PortkeyApiPaths.CHAT_COMPLETE_API,
            body=body,
            params=None,
            cast_to=ChatCompletions,
            stream_cls=Stream[ChatCompletionChunk],
            stream=stream,
            headers={},
        )

    def _get_config_string(self, config: Union[Mapping, str]) -> str:
        return config if isinstance(config, str) else json.dumps(config)


class AsyncCompletions(AsyncAPIResource):
    def __init__(self, client: AsyncAPIClient) -> None:
        super().__init__(client)

    @overload
    async def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        config: Optional[Union[Mapping, str]] = None,
        stream: Literal[True],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> AsyncStream[ChatCompletionChunk]:
        ...

    @overload
    async def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        config: Optional[Union[Mapping, str]] = None,
        stream: Literal[False] = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> ChatCompletions:
        ...

    @overload
    async def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        config: Optional[Union[Mapping, str]] = None,
        stream: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> Union[ChatCompletions, AsyncStream[ChatCompletionChunk]]:
        ...

    async def create(
        self,
        *,
        messages: Optional[List[Message]] = None,
        stream: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs,
    ) -> Union[ChatCompletions, AsyncStream[ChatCompletionChunk]]:
        body = dict(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_k=top_k,
            top_p=top_p,
            stream=stream,
            **kwargs,
        )

        return await self._post(
            PortkeyApiPaths.CHAT_COMPLETE_API,
            body=body,
            params=None,
            cast_to=ChatCompletions,
            stream_cls=AsyncStream[ChatCompletionChunk],
            stream=stream,
            headers={},
        )

    def _get_config_string(self, config: Union[Mapping, str]) -> str:
        return config if isinstance(config, str) else json.dumps(config)
