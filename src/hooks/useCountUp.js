import { useState, useEffect } from "react";

export function useCountUp(targetValue, durationMs = 1000) {
  const [currentValue, setCurrentValue] = useState(0);

  useEffect(() => {
    let animationFrameId;
    let startTimestamp;

    function tick(timestamp) {
      if (!startTimestamp) startTimestamp = timestamp;
      const elapsed = timestamp - startTimestamp;
      const rawProgress = Math.min(elapsed / durationMs, 1);
      const easedProgress = 1 - Math.pow(1 - rawProgress, 3);
      setCurrentValue(targetValue * easedProgress);
      if (rawProgress < 1) animationFrameId = requestAnimationFrame(tick);
    }

    animationFrameId = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(animationFrameId);
  }, [targetValue, durationMs]);

  return currentValue;
}
