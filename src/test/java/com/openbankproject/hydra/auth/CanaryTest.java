package com.openbankproject.hydra.auth;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * Canary test — confirms the test framework loads and runs.
 */
class CanaryTest {

    @Test
    @DisplayName("Test framework is operational")
    void testFrameworkLoads() {
        assertThat(true).isTrue();
    }

    @Test
    @DisplayName("JUnit 5 assertions work")
    void junitAssertionsWork() {
        assertThat(1 + 1).isEqualTo(2);
    }
}
