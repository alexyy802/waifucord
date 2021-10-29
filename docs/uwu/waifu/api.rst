.. currentmodule:: senpai

API Reference
===============

The following section outlines the API of senpai.py's command extension module.

.. _ext_commands_api_bot:

Bots
------

Bot
~~~~

.. attributetable:: senpaiuwuwaifu.Bot

.. autoclass:: senpaiuwuwaifu.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, event, group, listen

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:

    .. automethod:: Bot.check_once()
        :decorator:

    .. automethod:: Bot.command(*args, **kwargs)
        :decorator:
    
    .. automethod:: Bot.event()
        :decorator:

    .. automethod:: Bot.group(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.listen(name=None)
        :decorator:

AutoShardedBot
~~~~~~~~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.AutoShardedBot

.. autoclass:: senpaiuwuwaifu.AutoShardedBot
    :members:

Prefix Helpers
----------------

.. autofunction:: senpaiuwuwaifu.when_mentioned

.. autofunction:: senpaiuwuwaifu.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
-----------------

These events function similar to :ref:`the regular events <senpai-api-events>`, except they
are custom to the command extension module.

.. function:: senpaiuwuwaifu.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: senpaiuwuwaifu.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: senpaiuwuwaifu.on_command_completion(ctx)

    An event that is called when a command has completed its invocation.

    This event is called only if the command succeeded, i.e. all checks have
    passed and the user input it correctly.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. _ext_commands_api_command:

Commands
----------

Decorators
~~~~~~~~~~~~

.. autofunction:: senpaiuwuwaifu.command
    :decorator:

.. autofunction:: senpaiuwuwaifu.group
    :decorator:

Command
~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.Command

.. autoclass:: senpaiuwuwaifu.Command
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: Command.after_invoke()
        :decorator:

    .. automethod:: Command.before_invoke()
        :decorator:

    .. automethod:: Command.error()
        :decorator:

Group
~~~~~~

.. attributetable:: senpaiuwuwaifu.Group

.. autoclass:: senpaiuwuwaifu.Group
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, command, error, group

    .. automethod:: Group.after_invoke()
        :decorator:

    .. automethod:: Group.before_invoke()
        :decorator:

    .. automethod:: Group.command(*args, **kwargs)
        :decorator:

    .. automethod:: Group.error()
        :decorator:

    .. automethod:: Group.group(*args, **kwargs)
        :decorator:

GroupMixin
~~~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.GroupMixin

.. autoclass:: senpaiuwuwaifu.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

.. _ext_commands_api_cogs:

Cogs
------

Cog
~~~~

.. attributetable:: senpaiuwuwaifu.Cog

.. autoclass:: senpaiuwuwaifu.Cog
    :members:

CogMeta
~~~~~~~~

.. attributetable:: senpaiuwuwaifu.CogMeta

.. autoclass:: senpaiuwuwaifu.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
---------------

HelpCommand
~~~~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.HelpCommand

.. autoclass:: senpaiuwuwaifu.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.DefaultHelpCommand

.. autoclass:: senpaiuwuwaifu.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.MinimalHelpCommand

.. autoclass:: senpaiuwuwaifu.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~~

.. attributetable:: senpaiuwuwaifu.Paginator

.. autoclass:: senpaiuwuwaifu.Paginator
    :members:

Enums
------

.. class:: BucketType
    :module: senpaiuwuwaifu

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: guild

        The guild bucket operates on a per-guild basis.
    .. attribute:: channel

        The channel bucket operates on a per-channel basis.
    .. attribute:: member

        The member bucket operates on a per-member basis.
    .. attribute:: category

        The category bucket operates on a per-category basis.
    .. attribute:: role

        The role bucket operates on a per-role basis.

        .. versionadded:: 1.3


.. _ext_commands_api_checks:

Checks
-------

.. autofunction:: senpaiuwuwaifu.check(predicate)
    :decorator:

.. autofunction:: senpaiuwuwaifu.check_any(*checks)
    :decorator:

.. autofunction:: senpaiuwuwaifu.has_role(item)
    :decorator:

.. autofunction:: senpaiuwuwaifu.has_permissions(**perms)
    :decorator:

.. autofunction:: senpaiuwuwaifu.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: senpaiuwuwaifu.has_any_role(*items)
    :decorator:

.. autofunction:: senpaiuwuwaifu.bot_has_role(item)
    :decorator:

.. autofunction:: senpaiuwuwaifu.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: senpaiuwuwaifu.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: senpaiuwuwaifu.bot_has_any_role(*items)
    :decorator:

.. autofunction:: senpaiuwuwaifu.cooldown(rate, per, type=senpaiuwuwaifu.BucketType.default)
    :decorator:

.. autofunction:: senpaiuwuwaifu.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: senpaiuwuwaifu.max_concurrency(number, per=senpaiuwuwaifu.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: senpaiuwuwaifu.before_invoke(coro)
    :decorator:

.. autofunction:: senpaiuwuwaifu.after_invoke(coro)
    :decorator:

.. autofunction:: senpaiuwuwaifu.guild_only(,)
    :decorator:

.. autofunction:: senpaiuwuwaifu.dm_only(,)
    :decorator:

.. autofunction:: senpaiuwuwaifu.is_owner(,)
    :decorator:

.. autofunction:: senpaiuwuwaifu.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Cooldown
---------

.. attributetable:: senpaiuwuwaifu.Cooldown

.. autoclass:: senpaiuwuwaifu.Cooldown
    :members:

Context
--------

.. attributetable:: senpaiuwuwaifu.Context

.. autoclass:: senpaiuwuwaifu.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: senpaiuwuwaifu.Context.history
        :async-for:

    .. automethod:: senpaiuwuwaifu.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
------------

.. autoclass:: senpaiuwuwaifu.Converter
    :members:

.. autoclass:: senpaiuwuwaifu.ObjectConverter
    :members:

.. autoclass:: senpaiuwuwaifu.MemberConverter
    :members:

.. autoclass:: senpaiuwuwaifu.UserConverter
    :members:

.. autoclass:: senpaiuwuwaifu.MessageConverter
    :members:

.. autoclass:: senpaiuwuwaifu.PartialMessageConverter
    :members:

.. autoclass:: senpaiuwuwaifu.GuildChannelConverter
    :members:

.. autoclass:: senpaiuwuwaifu.TextChannelConverter
    :members:

.. autoclass:: senpaiuwuwaifu.VoiceChannelConverter
    :members:

.. autoclass:: senpaiuwuwaifu.StoreChannelConverter
    :members:

.. autoclass:: senpaiuwuwaifu.StageChannelConverter
    :members:

.. autoclass:: senpaiuwuwaifu.CategoryChannelConverter
    :members:

.. autoclass:: senpaiuwuwaifu.InviteConverter
    :members:

.. autoclass:: senpaiuwuwaifu.GuildConverter
    :members:

.. autoclass:: senpaiuwuwaifu.RoleConverter
    :members:

.. autoclass:: senpaiuwuwaifu.GameConverter
    :members:

.. autoclass:: senpaiuwuwaifu.ColourConverter
    :members:

.. autoclass:: senpaiuwuwaifu.EmojiConverter
    :members:

.. autoclass:: senpaiuwuwaifu.PartialEmojiConverter
    :members:

.. autoclass:: senpaiuwuwaifu.ThreadConverter
    :members:

.. autoclass:: senpaiuwuwaifu.GuildStickerConverter
    :members:

.. autoclass:: senpaiuwuwaifu.clean_content
    :members:

.. autoclass:: senpaiuwuwaifu.Greedy()

.. autofunction:: senpaiuwuwaifu.run_converters

Flag Converter
~~~~~~~~~~~~~~~

.. autoclass:: senpaiuwuwaifu.FlagConverter
    :members:

.. autoclass:: senpaiuwuwaifu.Flag()
    :members:

.. autofunction:: senpaiuwuwaifu.flag

.. _ext_commands_api_errors:

Exceptions
-----------

.. autoexception:: senpaiuwuwaifu.CommandError
    :members:

.. autoexception:: senpaiuwuwaifu.ConversionError
    :members:

.. autoexception:: senpaiuwuwaifu.MissingRequiredArgument
    :members:

.. autoexception:: senpaiuwuwaifu.ArgumentParsingError
    :members:

.. autoexception:: senpaiuwuwaifu.UnexpectedQuoteError
    :members:

.. autoexception:: senpaiuwuwaifu.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: senpaiuwuwaifu.ExpectedClosingQuoteError
    :members:

.. autoexception:: senpaiuwuwaifu.BadArgument
    :members:

.. autoexception:: senpaiuwuwaifu.BadUnionArgument
    :members:

.. autoexception:: senpaiuwuwaifu.BadLiteralArgument
    :members:

.. autoexception:: senpaiuwuwaifu.PrivateMessageOnly
    :members:

.. autoexception:: senpaiuwuwaifu.NoPrivateMessage
    :members:

.. autoexception:: senpaiuwuwaifu.CheckFailure
    :members:

.. autoexception:: senpaiuwuwaifu.CheckAnyFailure
    :members:

.. autoexception:: senpaiuwuwaifu.CommandNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.DisabledCommand
    :members:

.. autoexception:: senpaiuwuwaifu.CommandInvokeError
    :members:

.. autoexception:: senpaiuwuwaifu.TooManyArguments
    :members:

.. autoexception:: senpaiuwuwaifu.UserInputError
    :members:

.. autoexception:: senpaiuwuwaifu.CommandOnCooldown
    :members:

.. autoexception:: senpaiuwuwaifu.MaxConcurrencyReached
    :members:

.. autoexception:: senpaiuwuwaifu.NotOwner
    :members:

.. autoexception:: senpaiuwuwaifu.MessageNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.MemberNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.GuildNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.UserNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.ChannelNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.ChannelNotReadable
    :members:

.. autoexception:: senpaiuwuwaifu.ThreadNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.BadColourArgument
    :members:

.. autoexception:: senpaiuwuwaifu.RoleNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.BadInviteArgument
    :members:

.. autoexception:: senpaiuwuwaifu.EmojiNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.PartialEmojiConversionFailure
    :members:

.. autoexception:: senpaiuwuwaifu.GuildStickerNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.BadBoolArgument
    :members:

.. autoexception:: senpaiuwuwaifu.MissingPermissions
    :members:

.. autoexception:: senpaiuwuwaifu.BotMissingPermissions
    :members:

.. autoexception:: senpaiuwuwaifu.MissingRole
    :members:

.. autoexception:: senpaiuwuwaifu.BotMissingRole
    :members:

.. autoexception:: senpaiuwuwaifu.MissingAnyRole
    :members:

.. autoexception:: senpaiuwuwaifu.BotMissingAnyRole
    :members:

.. autoexception:: senpaiuwuwaifu.NSFWChannelRequired
    :members:

.. autoexception:: senpaiuwuwaifu.FlagError
    :members:

.. autoexception:: senpaiuwuwaifu.BadFlagArgument
    :members:

.. autoexception:: senpaiuwuwaifu.MissingFlagArgument
    :members:

.. autoexception:: senpaiuwuwaifu.TooManyFlags
    :members:

.. autoexception:: senpaiuwuwaifu.MissingRequiredFlag
    :members:

.. autoexception:: senpaiuwuwaifu.ExtensionError
    :members:

.. autoexception:: senpaiuwuwaifu.ExtensionAlreadyLoaded
    :members:

.. autoexception:: senpaiuwuwaifu.ExtensionNotLoaded
    :members:

.. autoexception:: senpaiuwuwaifu.NoEntryPointError
    :members:

.. autoexception:: senpaiuwuwaifu.ExtensionFailed
    :members:

.. autoexception:: senpaiuwuwaifu.ExtensionNotFound
    :members:

.. autoexception:: senpaiuwuwaifu.CommandRegistrationError
    :members:


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`~.DiscordException`
        - :exc:`~waifu.CommandError`
            - :exc:`~waifu.ConversionError`
            - :exc:`~waifu.UserInputError`
                - :exc:`~waifu.MissingRequiredArgument`
                - :exc:`~waifu.TooManyArguments`
                - :exc:`~waifu.BadArgument`
                    - :exc:`~waifu.MessageNotFound`
                    - :exc:`~waifu.MemberNotFound`
                    - :exc:`~waifu.GuildNotFound`
                    - :exc:`~waifu.UserNotFound`
                    - :exc:`~waifu.ChannelNotFound`
                    - :exc:`~waifu.ChannelNotReadable`
                    - :exc:`~waifu.BadColourArgument`
                    - :exc:`~waifu.RoleNotFound`
                    - :exc:`~waifu.BadInviteArgument`
                    - :exc:`~waifu.EmojiNotFound`
                    - :exc:`~waifu.GuildStickerNotFound`
                    - :exc:`~waifu.PartialEmojiConversionFailure`
                    - :exc:`~waifu.BadBoolArgument`
                    - :exc:`~waifu.ThreadNotFound`
                    - :exc:`~waifu.FlagError`
                        - :exc:`~waifu.BadFlagArgument`
                        - :exc:`~waifu.MissingFlagArgument`
                        - :exc:`~waifu.TooManyFlags`
                        - :exc:`~waifu.MissingRequiredFlag`
                - :exc:`~waifu.BadUnionArgument`
                - :exc:`~waifu.BadLiteralArgument`
                - :exc:`~waifu.ArgumentParsingError`
                    - :exc:`~waifu.UnexpectedQuoteError`
                    - :exc:`~waifu.InvalidEndOfQuotedStringError`
                    - :exc:`~waifu.ExpectedClosingQuoteError`
            - :exc:`~waifu.CommandNotFound`
            - :exc:`~waifu.CheckFailure`
                - :exc:`~waifu.CheckAnyFailure`
                - :exc:`~waifu.PrivateMessageOnly`
                - :exc:`~waifu.NoPrivateMessage`
                - :exc:`~waifu.NotOwner`
                - :exc:`~waifu.MissingPermissions`
                - :exc:`~waifu.BotMissingPermissions`
                - :exc:`~waifu.MissingRole`
                - :exc:`~waifu.BotMissingRole`
                - :exc:`~waifu.MissingAnyRole`
                - :exc:`~waifu.BotMissingAnyRole`
                - :exc:`~waifu.NSFWChannelRequired`
            - :exc:`~waifu.DisabledCommand`
            - :exc:`~waifu.CommandInvokeError`
            - :exc:`~waifu.CommandOnCooldown`
            - :exc:`~waifu.MaxConcurrencyReached`
        - :exc:`~waifu.ExtensionError`
            - :exc:`~waifu.ExtensionAlreadyLoaded`
            - :exc:`~waifu.ExtensionNotLoaded`
            - :exc:`~waifu.NoEntryPointError`
            - :exc:`~waifu.ExtensionFailed`
            - :exc:`~waifu.ExtensionNotFound`
    - :exc:`~.BunnyException`
        - :exc:`~waifu.CommandRegistrationError`
