from client import ServerlessColdstartGpuMicrocontainerAutoscalerClient

def main():
    client = ServerlessColdstartGpuMicrocontainerAutoscalerClient()
    res = client.route_inference_to_warm_gpu('sha256:qwen2.5-coder-32b-instruct', 16)
    print('GPU Routing ID: ' + res['routing_decision_id'] + ' -> ' + res['target_gpu_cluster'])
    print('Cold Start Restore: ' + str(res['cold_start_snapshot_restore_ms']) + 'ms | Pinned Pages: ' + str(res['shared_memory_pages_pinned']))
    print('Zero Idle Cost: ' + str(res['zero_idle_cost_achieved']) + ' | Telemetry: ' + res['gpu_telemetry_endpoint'])

if __name__ == '__main__':
    main()
