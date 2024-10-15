# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 CERN.
#
# Invenio-RDM is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.
"""Collections schema."""

from marshmallow import Schema, fields


class CollectionSchema(Schema):
    """Collection schema."""

    slug = fields.Str()
    title = fields.Str()
    depth = fields.Int()
    order = fields.Int()
    id = fields.Int()
    num_records = fields.Int()
