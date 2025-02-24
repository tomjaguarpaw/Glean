/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */


#include "glean/rts/prim.h"
#include "glean/rts/binary.h"

namespace facebook {
namespace glean {
namespace rts {

void relToAbsByteSpans(folly::ByteRange range, binary::Output& output) {
  auto input = binary::Input(range);

  // Read the length of the given array of relative byte spans and write it to the output
  const uint64_t length = input.packed<uint64_t>();
  output.packed(length);

  // Read the packed relative byte spans and write the absolute spans
  // The first relative byte span contains the start position
  uint64_t start = 0;
  for (auto i = 0; i < length; i++) {
    auto offset = input.packed<uint64_t>();
    start += offset;
    output.packed(start);
    output.packed(input.packed<uint64_t>());
  }
}
}
}
}
