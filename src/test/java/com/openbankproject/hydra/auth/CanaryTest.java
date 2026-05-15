package com.openbankproject.hydra.auth;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class CanaryTest {

    @Test
    @DisplayName("Canary: test framework loads and assertions work")
    void canary() {
        assertThat(true).isTrue();
    }
}
