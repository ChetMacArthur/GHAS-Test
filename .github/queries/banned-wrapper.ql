/**
 * @name Usage of Banned Hash Wrapper
 * @description Detects calls to the internal 'unsafe_hash_algo' function.
 * @kind problem
 * @problem.severity error
 * @id python/custom/banned-wrapper
 * @tags security
 */

import python

from Call c
where c.getFunc().(Name).getId() = "unsafe_hash_algo"
select c, "VIOLATION: Do not use the banned 'unsafe_hash_algo' wrapper."
