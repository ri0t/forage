#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# FOREACH
# =======
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup

setup(
    name="forage",
    description="forage",
    version="1.0.0",
    author="Heiko 'riot' Weinen",
    author_email="riot@c-base.org",
    license="GNU Affero General Public License v3",
    scripts=[
        'forage',
    ],
    long_description="""forage
=======

A tool to run a command on given folders.""",
    install_requires=[
        'click>=6.7.0',
        'spur>=0.3.20'
    ],
    entry_points="""[console_scripts]
    forage=foreach:main"""
)
