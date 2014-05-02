# This file is part of Pebble.

# Pebble is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.

# Pebble is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Pebble.  If not, see <http://www.gnu.org/licenses/>.


import signal

from functools import wraps


def synchronized(lock):
    """Locks the execution of decorated function on given *lock*.

    Works with both threading and multiprocessing Lock.

    """
    def wrap(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            with lock:
                return function(*args, **kwargs)

        return wrapper

    return wrap


def signal_handler(signals):
    """Sets the decorated function as signal handler of given *signals*.

    *signals* can be either a single signal or a list/tuple
    of multiple ones.

    """
    def wrap(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if isinstance(signals, (list, tuple)):
                for signum in signals:
                    signal.signal(signum, function)
            else:
                signal.signal(signals, function)

        return wrapper

    return wrap
