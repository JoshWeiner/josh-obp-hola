package com.openbankproject.hydra.auth;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class CanaryTest {

    @Test
    @DisplayName("Canary — JUnit 5 + AssertJ are correctly wired")
    void frameworkLoads() {
        assertThat(true).isTrue();
    }

    @Test
    @DisplayName("Canary — Mockito is on the classpath")
    void mockitoAvailable() {
        assertThat(org.mockito.Mockito.class).isNotNull();
    }
}
