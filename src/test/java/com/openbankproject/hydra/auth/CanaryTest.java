package com.openbankproject.hydra.auth;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

/**
 * Canary test that verifies the test framework (JUnit 5, AssertJ, Mockito) loads correctly.
 */
class CanaryTest {

    @Test
    void junitAndAssertjWork() {
        assertThat(1 + 1).isEqualTo(2);
    }

    @Test
    void mockitoWorks() {
        Runnable mockRunnable = mock(Runnable.class);
        when(mock(Comparable.class).compareTo("a")).thenReturn(42);
        assertThat(mockRunnable).isNotNull();
    }
}
